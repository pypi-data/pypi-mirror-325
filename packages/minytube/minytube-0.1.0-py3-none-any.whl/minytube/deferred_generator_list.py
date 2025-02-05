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
from typing import Any, Iterable, List, Union

logger = logging.getLogger(__name__)

class DeferredGeneratorList:
    """
    A lazy list that yields items from a generator on demand.
    Avoids recursion in __getitem__ or __len__.

    Example usage:
        items = DeferredGeneratorList(generator)
        # items[:10], len(items), iteration, etc. all possible.
    """

    def __init__(self, generator: Iterable[Any]) -> None:
        self._generator = iter(generator)
        self._list: List[Any] = []
        self._exhausted = False

    def __iter__(self) -> Iterable[Any]:
        # yield from cached first
        for item in self._list:
            yield item
        # then from the generator
        if not self._exhausted:
            for item in self._generator:
                self._list.append(item)
                yield item
            self._exhausted = True

    def _ensure_index(self, index: int) -> None:
        """
        Generate items up to the 'index' (inclusive if possible).
        """
        while len(self._list) <= index and not self._exhausted:
            try:
                self._list.append(next(self._generator))
            except StopIteration:
                self._exhausted = True
                break

    def __getitem__(self, index: Union[int, slice]) -> Any:
        if isinstance(index, slice):
            start, stop, step = index.indices(10**9)
            if stop < 0:
                stop = len(self._list) + stop
            self._ensure_index(stop - 1)
            return self._list[index]
        else:
            self._ensure_index(index)
            return self._list[index]

    def __len__(self) -> int:
        """
        Exhaust the generator to find length.
        """
        if not self._exhausted:
            for item in self._generator:
                self._list.append(item)
            self._exhausted = True
        return len(self._list)
