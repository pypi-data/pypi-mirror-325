from datetime import datetime
from http import HTTPStatus
from pathlib import Path
from time import sleep

import requests

from provider_switch.constants.core_constants import Constant
from provider_switch.exceptions import (
    BadProviderException,
    BadRequestException,
    ExitException,
    ProviderErrorException,
)
from provider_switch.helpers.common_helper import CommonHelper
from provider_switch.helpers.response_helper import ResponseHelper
from provider_switch.models.provider_model import ProviderModel
from provider_switch.provider_collection import ProviderCollection
from provider_switch.utils.notify_service import NotifyService
from json import dumps


class ProviderSwitchHandler(object):
    service_name = None
    allowed_content_type = ["application/json", "application/json; charset=utf-8"]

    def __init__(self, service_name: str, social_type: str, **kwargs):
        self.service_name = service_name
        self.social_type = social_type
        self.allowed_providers = kwargs.get("allowed_providers", None)
        self.is_pagination = kwargs.get("is_pagination", False)
        self.num_of_pages = kwargs.get("num_of_pages", 1)
        self.retry_when_not_found = kwargs.get("retry_when_not_found", False)
        self.providers = []
        self.current_provider = None
        self.driver_type = kwargs.get("driver_type", "ssm")
        self.root_path = kwargs.get("root_path", None)
        self.boto3_session = kwargs.get("boto3_session", None)
        self.notify_service = NotifyService(
            channels=[
                {
                    "type": "webhook",
                    "webhook_url": "https://chat.googleapis.com/v1/spaces/AAAAoFde3Ho/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=xGDDaCfjzmbRPTdGU2gjjtmLb-bffbm5JamLTNFrlI8",
                }
            ],
            timestamp=False,
        )
        self._prepare()

    def _prepare(self) -> None:
        # print(Path(__file__))
        # print('Start prepare', datetime.now())
        providers = ProviderCollection(
            driver_type=self.driver_type,
            social_type=self.social_type,
            service_name=self.service_name,
            retry_when_not_found=self.retry_when_not_found,
            root_path=self.root_path,
            boto3_session=self.boto3_session,
        ).get_providers()
        if self.allowed_providers is not None:
            providers = [
                provider
                for provider in providers
                if provider.name in self.allowed_providers
            ]

        self.providers = providers
        # print('End  prepare', datetime.now())

    def _get_best_provider(self) -> ProviderModel:
        """Get best provider

        Raises:
            Exception: _description_

        Returns:
            ProviderModel: _description_
        """
        for provider in self.providers:
            if provider.is_good():
                return provider

        raise Exception("No provider available")

    def _request(
        self,
        method: str,
        url: str,
        headers: dict,
        params: dict,
        timeout: int = None,
        body: dict = None,
    ) -> dict:  # noqa: C901
        request_specs = self.current_provider.get_attr("request.specs")
        has_pagination = False

        pagination = request_specs.get("pagination", None)

        if pagination is not None:
            cursor_field = pagination.get("cursor_field", None)
            cursor_append_to = pagination.get("cursor_append_to", None)
            cursor_default_value = pagination.get("cursor_default_value", None)

            if (
                cursor_field is not None
                and cursor_append_to is not None
                and cursor_default_value is not None
            ):
                has_pagination = True

        if has_pagination is True:
            if cursor_append_to == "path":
                url = url + "/" + cursor_default_value

            if cursor_append_to == "param":
                params[cursor_field] = cursor_default_value
        try:
            response = getattr(requests, method)(
                url=url, headers=headers, params=params, timeout=timeout, json=body
            )
        except Exception as exc:
            if Constant.TIMEOUT_ERROR_TEXT in str(exc):
                raise BadRequestException(
                    status=0, http_status_code=500, message="Error", retry=True
                )
        status_code = response.status_code if response is not None else None
        response_headers = response.headers if response is not None else None
        content_type = (
            response_headers.get("content-type") if response_headers else None
        )
        provider_data = {}
        rate_limit_keys = self.current_provider.config.get("rate_limit_keys", None)

        # print('------------------')
        # print('Status code: ', status_code)
        # print('------------------')

        if rate_limit_keys is not None and response_headers is not None:
            rate_limit_quotas_key = rate_limit_keys.get("rate_limit_quotas_key", 0)
            rate_limit_remaining_key = rate_limit_keys.get(
                "rate_limit_remaining_key", 0
            )
            rate_limit_refresh_key = rate_limit_keys.get("rate_limit_refresh_key", 0)

            quotas = int(response_headers.get(rate_limit_quotas_key, 0))
            quotas_remaining = int(response_headers.get(rate_limit_remaining_key, 0))
            quota_refresh_time = int(response_headers.get(rate_limit_refresh_key, 0))

            if not quotas and not quotas_remaining and not quota_refresh_time:
                provider_data = {
                    "quotas": quotas,
                    "quotas_remaining": quotas_remaining,
                    "quota_refresh_time": quota_refresh_time,
                }

        encoded_content = response.content.decode("utf-8")
        if encoded_content == "":
            raise ProviderErrorException(
                status=0,
                http_status_code=status_code,
                service_name=self.service_name,
                provider_name=self.current_provider.name,
                response={"REQUEST_URL": response.request.url},
            )

        response_json = response.json()

        print("Status code: ", status_code)
        # print('Header: ', response_headers)
        # print('Body: ', body)

        if status_code == HTTPStatus.NOT_FOUND:
            raise ExitException(status=0, http_status_code=status_code)

        if (
            status_code != HTTPStatus.OK
            or content_type not in self.allowed_content_type
        ):
            raise BadRequestException(
                status=0,
                http_status_code=status_code,
                message=response_json.get("message") or "Error",
                retry=True,
                provider_data=provider_data,
            )

        validated = self.current_provider.check_response(response_json)

        if validated["status"] is False:
            if validated["retry"] is True:
                raise BadRequestException(
                    status=0,
                    http_status_code=500,
                    message="Error",
                    retry=True,
                    provider_data=provider_data,
                )
            else:
                raise ExitException(
                    status=0,
                    http_status_code=500,
                )

        self.current_provider.increment_session_success()
        # try:
        #     print('Sync parameter')
        #     # self.current_provider.sync(provider_data)
        # except Exception as e:
        #     print(f'Error sync parameter: {str(e)}')

        return ResponseHelper(self.current_provider).standardize_response(response_json)

    def _multiple_requests(
        self, method: str, url: str, headers: dict, params: dict, body: dict
    ) -> dict:
        """Multiple requests

        Args:
            variables (dict, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        response = []

        for i in range(self.num_of_pages):
            response.append(
                self._request(
                    method=method, url=url, headers=headers, params=params, body=body
                )
            )

        return response

    def _make_request(self, variables: dict) -> dict:  # noqa: C901
        """Make request to RapidAPI

        Args:
            variables (dict): Variables

        Raises:
            BadProviderException: Bad provider exception
            BadRequestException: Bad request exception
            ExitException: Exit exception

        Returns:
            dict: Response
        """
        try:
            params = {}
            method = ""
            url = ""
            provider = self._get_best_provider()
            self.current_provider = provider
            request_specs = provider.get_attr("request.specs")

            url = provider.get_attr("url")
            method = request_specs.get("method", "get")
            req_headers = provider.get_attr("headers")
            session_fail = provider.get_attr("session_fail")
            timeout = (
                int(provider.get_attr("timeout"))
                if provider.get_attr("timeout")
                else None
            )

            if session_fail == provider.retry_time:
                raise BadProviderException(switch_provider=True)

            params = provider.get_attr("request.specs.params")
            json_payload = provider.get_attr("request.specs.body")

            # print('Provider: ', provider.name)
            print("URL: ", url)
            # print('Method: ', method)
            # print('Params: ', params)
            print("Variables: ", variables)

            if variables:
                url = CommonHelper.format_data(url, variables)

                if params:
                    for param in params:
                        params[param] = variables.get(params[param], None)

                if json_payload:
                    for json_payload_item in json_payload:
                        json_payload[json_payload_item] = variables.get(
                            json_payload[json_payload_item], None
                        )

            if self.is_pagination is True:
                return self._multiple_requests(
                    method=method,
                    url=url,
                    headers=req_headers,
                    params=params,
                    body=json_payload,
                )

            return self._request(
                method=method,
                url=url,
                headers=req_headers,
                params=params,
                timeout=timeout,
                body=json_payload,
            )
        except ProviderErrorException as e:
            self.notify_service.error(
                self.service_name,
                self.current_provider.name if self.current_provider else "UNKNOWN",
                dumps(
                    {
                        "EXCEPTION": "BadProviderException: must_retry",
                        "REQUEST": {
                            "method": method,
                            "url": url,
                            "params": params,
                        },
                        "RESPONSE": e.response,
                    }
                ),
            )
            print(
                "ProviderErrorException: ", e.service_name, e.provider_name, e.response
            )
            return {
                "error": True,
                "exception": "ProviderErrorException",
                "trace": {
                    "provider_name": e.provider_name,
                    "provider_name": e.provider_name,
                },
            }

        except BadRequestException as e:
            self.notify_service.error(
                self.service_name,
                self.current_provider.name if self.current_provider else "UNKNOWN",
                dumps(
                    {
                        "EXCEPTION": "BadProviderException: must_retry",
                        "REQUEST": {
                            "method": method,
                            "url": url,
                            "params": params,
                        },
                        "RESPONSE": str(e.message),
                    }
                ),
            )
            print("BadRequestException: ", e.message)
            if e.must_retry():
                print("BadRequestException must_retry")
                sleep(provider.retry_delay or 3)
                provider.increment_session_fail()
                return self._make_request(variables)
            else:
                return None

        except BadProviderException as e:
            self.notify_service.error(
                self.service_name,
                self.current_provider.name if self.current_provider else "UNKNOWN",
                dumps(
                    {
                        "EXCEPTION": "BadProviderException: must_switch_provider",
                        "REQUEST": {
                            "method": method,
                            "url": url,
                            "params": params,
                        },
                        "RESPONSE": str(e.message),
                    }
                ),
            )
            print("BadProviderException: ", e.message)
            if e.must_switch_provider():
                print("BadProviderException must_switch_provider")
                try:
                    provider.set_inactive()
                except Exception as e:
                    print(f"Error sync parameter: {str(e)}")
                return self._make_request(variables)
            else:
                return None

        except ExitException as e:
            self.notify_service.error(
                self.service_name,
                self.current_provider.name if self.current_provider else "UNKNOWN",
                dumps(
                    {
                        "EXCEPTION": "ExitException",
                        "REQUEST": {
                            "method": method,
                            "url": url,
                            "params": params,
                        },
                        "RESPONSE": str(e.message),
                    }
                ),
            )
            print("ExitException: ", e.message)
            return None

        except Exception as e:
            self.notify_service.error(
                self.service_name,
                self.current_provider.name if self.current_provider else "UNKNOWN",
                dumps(
                    {
                        "EXCEPTION": "CommonException",
                        "REQUEST": {
                            "method": method,
                            "url": url,
                            "params": params,
                        },
                        "RESPONSE": str(e),
                    }
                ),
            )
            print("Exception: ", e)
            return None

    def _refresh_providers(self):
        for i in range(len(self.providers)):
            self.providers[i].set_active()
            self.providers[i].refresh_session_fail()

    def get(self, variables: dict = None) -> dict:
        """GET request

        Args:
            variables (dict, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        result = self._make_request(variables=variables or {})
        self._refresh_providers()
        return result
