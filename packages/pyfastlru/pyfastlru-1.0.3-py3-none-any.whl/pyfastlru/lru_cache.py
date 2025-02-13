# pyfastlru v. 1.0
# Thread-safe LRU cache with the MutableMapping interface.
# SPDX-FileCopyrightText: Copyright © 2025 Anatoly Petrov <petrov.projects@gmail.com>
# SPDX-License-Identifier: MIT

"""Lru cache (thread-safe)."""

import collections
from collections.abc import MutableMapping, Hashable
import contextlib
import dataclasses
import threading
from typing import Any, Final, Iterator, NamedTuple, override, Self


class _ListNode:
    """Linked list node (internal)."""

    __slots__ = ["data", "prev", "next"]

    def __init__(
        self,
        data: Any | None = None,
        prev: Self | None = None,
        next: Self | None = None,
    ):
        self.data = data
        self.prev = prev
        self.next = next


class _LinkedList:
    """Linked list for item usage tracking (internal).

    The interface is limited only by methods needed to implement the lru cache.
    """

    def __init__(self):
        self._first: _ListNode | None = None
        self._last: _ListNode | None = None
        self._tot = 0

    def __bool__(self) -> bool:
        return self._size != 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        curr = self._first
        while curr is not None:
            # curr.next may be modified when yielding (e.g. on removing),
            # so we get the succeeding node here
            succ = curr.next
            yield curr
            curr = succ

    @property
    def front(self) -> _ListNode:
        """First list node.

        Raises:
            IndexError: If list is empty.
        """
        if self._first is None:
            raise IndexError("List is empty")
        # Ok
        return self._first

    @property
    def back(self) -> _ListNode:
        """Last list node.

        Raises:
            IndexError: If list is empty.
        """
        if self._last is None:
            raise IndexError("List is empty")
        # Ok
        return self._last

    def appendleft(self, data: Any) -> _ListNode:
        """Create node with the desired data at the beginning of the list."""
        node = _ListNode(data=data)
        self._appendleft(node)
        return node

    def touch(self, node: _ListNode) -> None:
        """Move the desired node to the beginning of the list."""
        if node is self._first:
            return
        node = self._remove(node)
        self._appendleft(node)

    def pop(self, node: _ListNode | None = None) -> _ListNode:
        """Remove and return the desired node from the list (last node if not specified)."""
        if node is None:
            node = self.back
        return self._remove(node)

    def clear(self):
        """Clear the list."""
        for node in self:
            self._remove(node)

    @property
    def _size(self):
        assert self._tot >= 0
        return self._tot

    def _appendleft(self, node: _ListNode) -> _ListNode:
        node.prev = None
        node.next = self._first
        if self._first is not None:
            self._first.prev = node
        self._first = node
        if self._last is None:
            self._last = node
        self._tot += 1
        return node

    def _remove(self, node: _ListNode) -> _ListNode:
        if self._size == 0:
            raise ValueError("Node already removed")
        prev_node, next_node = node.prev, node.next
        if prev_node is not None and next_node is not None:  # middle node
            prev_node.next = next_node
            next_node.prev = prev_node
        elif next_node is not None:  # has next, no prev -> first node
            next_node.prev = None
            self._first = next_node
        elif prev_node is not None:  # has prev, no next -> last node
            prev_node.next = None
            self._last = prev_node
        else:  # no prev and next -> single node
            self._first = None
            self._last = None
        # Prevents cycling references and GC-related issues
        node.prev = None
        node.next = None
        self._tot -= 1
        return node


@dataclasses.dataclass(slots=True)
class _CacheItem[Value]:
    """Cache item (internal)."""

    data: Value
    node: _ListNode


CacheInfo = collections.namedtuple(
    "_CacheInfo", ["hits", "misses", "maxsize", "currsize"]
)
"""Cache statistics."""


class CacheItem[Key, Value](NamedTuple):
    """Cache item as a key/value pair."""

    key: Key
    value: Value


class LruCache[Key: Hashable, Value](
    MutableMapping[Key, Value], contextlib.AbstractContextManager
):
    """Lru cache (thread-safe).

    Provides a `MutableMapping` interface similar to the `dict`.

    However, unlike a regular `dict`, which has no size limits, the cache size
    is restricted by the `maxsize` parameter specified during the initialization
    of the cache (defaulting to `128`). When the number of items exceeds this limit,
    the `LruCache` automatically removes the least recently used item to make space
    for new entries.

    Also, unlike a standard `dict`, which maintains a FIFO (first-in, first-out) order,
    the cache employs an MRU (most recently used) order. As a result, all iterators
    provided by the `LruCache` — including those from the `__iter__`, `keys`, `values`,
    and `items` methods — iterate from the MRU (most recently used) item to the LRU
    (least recently used) item.

    Cache synchronization is handled internally using a reentrant lock,
    so no action is needed from the end user. Manual synchronization with the `LruCache`
    context manager or through the `acquire` and `release` methods is only necessary
    for implementing atomic operations.

    The cache gathers usage statistics, including `hits`, `misses`, `maxsize`, and `currsize`,
    which can be accessed using the `cache_info()` method.
    """

    def __init__(self, maxsize=128):
        """Create a new cache instance limited by maxsize items."""
        if maxsize < 1:
            raise ValueError(f"Wrong cache maxsize: {maxsize}")
        self._cache: dict[Key, _CacheItem[Value]] = {}
        self._list = _LinkedList()
        self._lock = threading.RLock()
        self._maxsize: Final = maxsize
        self._hits = 0
        self._misses = 0

    def __getitem__(self, key: Key) -> Value:
        """Return an item that has the specified key."""
        with self._lock:
            try:
                item = self._cache[key]
                val, node = item.data, item.node
                self._hits += 1
            except KeyError:
                self._misses += 1
                raise
            self._list.touch(node)
            return val

    def __setitem__(self, key: Key, value: Value) -> None:
        """Store an item at the given key."""
        with self._lock:
            if (item := self._cache.get(key, None)) is not None:
                item.data = value
                self._list.touch(item.node)
                return
            # not found
            node = self._list.appendleft(key)
            self._cache[key] = _CacheItem(value, node)
            if len(self._cache) > self._maxsize:
                self.popitem()
                self._hits -= 1  # popitem affects cache statistics

    def __delitem__(self, key: Key) -> None:
        """Remove an item at the given key."""
        with self._lock:
            item = self._cache.pop(key)
            self._list.pop(item.node)
            return item.data

    def __iter__(self) -> Iterator[Key]:
        """Iterate over the cache keys in MRU-first order."""
        with self._lock:
            for node in self._list:
                yield node.data

    def __len__(self) -> int:
        """Return the cache length."""
        with self._lock:
            assert len(self._cache) == len(self._list), "Out of sync"
            return len(self._cache)

    def __enter__(self) -> Self:
        """Acquire the cache lock."""
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Release the cache lock."""
        self._lock.release()
        return False  # re-raise exception (if any)

    @property
    def front(self) -> CacheItem[Key, Value]:
        """Return an MRU item without touching LRU order.

        Raises:
            KeyError: If cache is empty.
        """
        with self._lock:
            try:
                key = self._list.front.data
            except IndexError:
                msg = "It is not possible to retrieve an item from an empty cache"
                raise KeyError(msg) from None
            val = self._cache[key].data
            return CacheItem(key, val)

    @property
    def back(self) -> CacheItem[Key, Value]:
        """Return an LRU item without touching LRU order.

        This item will be removed first if the cache exceeds the size limit.

        Raises:
            KeyError: If cache is empty.
        """
        with self._lock:
            try:
                key = self._list.back.data
            except IndexError:
                msg = "It is not possible to retrieve an item from an empty cache"
                raise KeyError(msg) from None
            val = self._cache[key].data
            return CacheItem(key, val)

    def touch(self, key: Key) -> None:
        """Mark the desired item as an MRU without retrieving it.

        Raises:
            KeyError: If item is not found.
        """
        with self._lock:
            item = self._cache[key]
            self._list.touch(item.node)

    def touch_last(self) -> None:
        """Mark the LRU item as an MRU without retrieving it.

        Raises:
            KeyError: If cache is empty.
        """
        self.touch(self.back.key)

    def keys(self) -> Iterator[Key]:
        """Iterate over the cache keys in the MRU-first order."""
        return iter(self)

    def values(self) -> Iterator[Value]:
        """Iterate over the cache values in the MRU-first order."""
        with self._lock:
            for node in self._list:
                key = node.data
                val = self._cache[key].data
                yield val

    def items(self) -> Iterator[CacheItem[Key, Value]]:
        """Iterate over the cache key/value pairs in the MRU-first order."""
        with self._lock:
            for node in self._list:
                key = node.data
                val = self._cache[key].data
                yield CacheItem(key, val)

    @override
    def popitem(self) -> CacheItem[Key, Value]:
        """Remove and return a (key, value) pair from the cache in LRU order.

        Raises:
            KeyError: If cache is empty.
        """
        with self._lock:
            item = self.back
            self.pop(item.key)
            return item

    def clear(self) -> None:
        """Clear the cache and statistics."""
        with self._lock:
            self._cache.clear()
            self._list.clear()
            self._hits = 0
            self._misses = 0

    def cache_info(self) -> CacheInfo:
        """Return the cache statistics."""
        with self._lock:
            return CacheInfo(
                hits=self._hits,
                misses=self._misses,
                maxsize=self._maxsize,
                currsize=len(self),
            )

    def acquire(self, blocking=True, timeout=-1) -> bool:
        """Manually acquire the cache lock."""
        return self._lock.acquire(blocking, timeout)

    def release(self) -> None:
        """Manually release the cache lock."""
        self._lock.release()
