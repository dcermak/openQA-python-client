# Copyright (C) 2015 Red Hat
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Adam Williamson <awilliam@redhat.com>
#          Ludwig Nussel   <ludwig.nussel@suse.de>
#          Jan Sedlak      <jsedlak@redhat.com>

"""Stubs for the openQA python client."""

import logging
import sys

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict
from typing import Any, Dict, List, NoReturn, Optional, Union, overload

import requests

logger: logging.Logger

RequestMethod = Literal["get", "put", "post", "delete", "GET", "PUT", "POST", "DELETE"]

class JobDict(TypedDict):
    settings: Dict[str, str]
    id: int
    clone_id: int

class OpenQA_Client:
    def __init__(self, server: str = "", scheme: str = "") -> None: ...
    def _add_auth_headers(self, request: requests.PreparedRequest) -> requests.PreparedRequest: ...
    @overload
    def do_request(
        self,
        request: requests.Request,
        retries: int = ...,
        wait: Union[int, float] = ...,
        parse: Literal[True] = ...,
    ) -> Any: ...
    @overload
    def do_request(
        self,
        request: requests.Request,
        retries: int = ...,
        wait: Union[int, float] = ...,
        parse: Literal[False] = ...,
    ) -> requests.Response: ...
    @overload
    def do_request(
        self,
        request: requests.Request,
        retries: int = ...,
        wait: Union[int, float] = ...,
        parse: bool = ...,
    ) -> Union[Any, requests.Response]: ...
    def openqa_request(
        self,
        method: RequestMethod,
        path: str,
        params: Any = ...,
        retries: int = ...,
        wait: int = ...,
        data: Any = ...,
    ) -> Any: ...
    def find_clones(self, jobs: List[JobDict]) -> List[JobDict]: ...
    @overload
    def get_jobs(
        self, jobs: Literal[None], build: Literal[None], filter_dupes: bool
    ) -> NoReturn: ...
    @overload
    def get_jobs(
        self, jobs: Optional[List[Union[str, int]]], build: Optional[str], filter_dupes: bool
    ) -> List[JobDict]: ...
