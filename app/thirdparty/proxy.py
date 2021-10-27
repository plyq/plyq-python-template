"""Describes different proxies to process HTTP-like requests."""

import abc
from typing import Any, Dict, Tuple

import requests


class Proxy(abc.ABC):
    """Proxy class for HTTP requests"""

    @abc.abstractmethod
    def get(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """Wrapper on GET request."""

    @abc.abstractmethod
    def post(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """Wrapper on POST request."""


class URLBaseProxy(Proxy):
    """Proxy to process requests."""

    def __init__(self, base_url: str) -> None:
        """
        :param url: base url for requests
        """
        self._base_url = base_url

    def get(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """
        Wrapper for ``requests.get().``

        :param request: request endpoint
        :param args: ``requests.get()`` other args
        :param kwargs: ``requests.get()`` other kwargs
        :returns: response data, response status
        """
        url = "%s/%s" % (self._base_url, request)
        response = requests.get(url, *args, **kwargs)
        return self._response_to_object(response)

    def post(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """
        Wrapper for ``requests.post().``

        :param request: request endpoint
        :param args: ``requests.post()`` other args
        :param kwargs: ``requests.post()`` other kwargs
        :returns: response data, response status
        """
        url = "%s/%s" % (self._base_url, request)
        response = requests.post(url, *args, **kwargs)
        return self._response_to_object(response)

    @staticmethod
    def _response_to_object(
        response: requests.models.Response,
    ) -> Tuple[Dict[str, Any], int]:
        """Transform response to human-readbale format.

        :param response: http response
        :returns: json and status
        """
        obj = (response.json(), response.status_code)
        return obj


class MirrorProxy(Proxy):
    """A mirror proxy"""

    STATUS = 1

    def get(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """
        Creates a dictionary with incoming arguments and returns it.

        Example of the result::
            {
                "method": "GET",
                "request": "incoming_request",
                "args": [1, "a"],
                "kwargs": {"b": 2}
            }

        :param request: request endpoint
        :param args: other args
        :param kwargs:  other kwargs
        :returns: arguments data, status is always 1
        """
        to_return = {
            "method": "GET",
            "request": request,
            "args": args,
            "kwargs": kwargs,
        }
        return to_return, self.STATUS

    def post(
        self, request: str, *args: Any, **kwargs: Any
    ) -> Tuple[Dict[str, Any], int]:
        """
        Creates a dictionary with incoming arguments and returns it.

        Example of the result::
            {
                "method": "POST",
                "request": "incoming_request",
                "args": [1, "a"],
                "kwargs": {"b": 2}
            }

        :param request: request endpoint
        :param args: other args
        :param kwargs:  other kwargs
        :returns: arguments data, status is always 1
        """
        to_return = {
            "method": "POST",
            "request": request,
            "args": args,
            "kwargs": kwargs,
        }
        return to_return, self.STATUS
