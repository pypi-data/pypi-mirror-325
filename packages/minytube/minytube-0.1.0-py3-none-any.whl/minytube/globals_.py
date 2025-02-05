"""
Copyright 2025 by Sergei Belousov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging

from .disk_cache import DiskCache
from .http_client import RequestsHttpClient
from .multi_fetcher import MultiFetcher

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

GLOBAL_CACHE = DiskCache("http_cache")
HTTP_CLIENT = RequestsHttpClient(cache=GLOBAL_CACHE)
MULTI_FETCHER = MultiFetcher(HTTP_CLIENT, max_workers=10)
