# Copyright (c) 2024, InfinityQ Technology, Inc.
import logging
import os
import requests

from pydantic import BaseModel, ValidationError
from typing import Any, Dict, Optional, Type
from urllib.parse import urljoin

import requests.adapters
import urllib3

from .model import CreditsResponse, SolveRequest, SolveResponse, TempStorageResponse
from ..errors import MissingTitanqApiKey, ServerError


log = logging.getLogger("TitanQ")

_QUEUED_STATUS = "Queued"
_TITANQ_API_VERSION = "v1"
_USER_AGENT_HEADER = 'User-Agent'

class Client:
    """
    TitanQ api client is a simple wrapper around TitanQ api to help interact with the
    service without the need to deal with http request
    """
    def __init__(self, api_key: Optional[str], base_server_url: str) -> None:
        api_key = api_key or os.getenv("TITANQ_API_KEY")
        if api_key is None:
            raise MissingTitanqApiKey(
                "No API key is provided. You can set your API key in the Model, "
                + "or you can set the environment variable TITANQ_API_KEY")
        self._server_url = base_server_url
        self._api_key = api_key


    def temp_storage(self) -> TempStorageResponse:
        """
        Query temporary storage url's

        :return: The temporary storage response

        :raises requests.exceptions.HTTPError: If an unexpected Error occur during request.
        """
        return self._do_http_request(f"{_TITANQ_API_VERSION}/temp_storage", response_type=TempStorageResponse)

    def credits(self) -> CreditsResponse:
        """
        Query Amount of credits remaining

        :return: The credit response.

        :raises requests.exceptions.HTTPError: If an unexpected Error occur during request.
        """
        return self._do_http_request(f"{_TITANQ_API_VERSION}/credits", response_type=CreditsResponse)

    def solve(self, request: SolveRequest) -> SolveResponse:
        """
        Issue a new solve request to the backend

        :param request: The solve request to issue to the solver

        :return: The response to the solve request (Not the response of the computation)

        :raises ServerError: If an unexpected Error occur during a solver request
        """
        log.debug(f"Issuing solve request to TitanQ server ({self._server_url}): {request}")
        response = self._do_http_request(f"{_TITANQ_API_VERSION}/solve", body=request, method='POST', response_type=SolveResponse)

        # something went wrong and the computation was not queued
        if response.status != _QUEUED_STATUS:
            log.error("An error occurred while issuing a solver request to the TitanQ server")
            raise ServerError(response.message)

        log.debug(f"Solve request response: {response}")
        return response


    def _do_http_request(
            self,
            path: str,
            *,
            headers: Dict[str, str] = {},
            body: BaseModel = None,
            method='GET',
            response_type: Type[BaseModel]
        ) -> Any:
        """
        Execute the actual http request to the TitanQ api while adding all defaults params

        :param headers: non-default header to the request.
        :param body: Body of the request.
        :param method: Which http method to use while performing the request.
        :param response_type: The object class that the json response will be cast to.

        :raise HTTPError: If the response cannot be created from the response type passed.

        :return: The response object created from the json response of the http request.
        """
        headers['authorization'] = self._api_key
        headers[_USER_AGENT_HEADER] = self._user_agent_string()
        url = urljoin(self._server_url, path)
        with requests.Session() as session:
            retries = urllib3.Retry(
                        total=3,
                        backoff_factor=0.5,
                        status_forcelist=[502, 503, 504, 495],
                        allowed_methods={"POST", "GET"},
                    )
            session.mount('https://', requests.adapters.HTTPAdapter(max_retries=retries))
            method = method.upper()
            if method=='GET':
                response = session.get(url, headers=headers)
            elif method=='POST':
                response = session.post(url, headers=headers, data=body.model_dump_json())
            else:
                raise NotImplementedError(f"http method: {method}")

            try:
                # create the response object from the response body
                return response_type.model_validate_json(response.content)
            except ValidationError:
                response.raise_for_status()
                raise

    def _user_agent_string(self) -> str:
        from titanq import __version__ as titanq_version # importing current module without cycle

        request_user_agent = requests.utils.default_headers().get(_USER_AGENT_HEADER, '')
        titanq_user_agent = f"TitanQ-sdk/{titanq_version} " + request_user_agent
        return titanq_user_agent.rstrip()