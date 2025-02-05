# pyfastlru v. 1.0
# Thread-safe LRU cache with the MutableMapping interface.
# SPDX-FileCopyrightText: Copyright © 2025 Anatoly Petrov <petrov.projects@gmail.com>
# SPDX-License-Identifier: MIT

"""Lru cache (thread-safe)."""

import collections
from collections.abc import MutableMapping
import contextlib
import dataclasses
import threading
from typing import Any, Final, Iterator, Self


class _ListNode:
    """Linked list node (internal)."""

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
        """Return the first node.

        Raises:
            IndexError: If list is empty.
        """
        if self._first is None:
            raise IndexError("List is empty")
        # Ok
        return self._first

    @property
    def back(self) -> _ListNode:
        """Return the last node.

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
        # Prevents cycling references and dangling nodes
        node.prev = None
        node.next = None
        self._tot -= 1
        return node


CacheInfo = collections.namedtuple(
    "_CacheInfo", ["hits", "misses", "maxsize", "currsize"]
)


@dataclasses.dataclass
class _CacheItem:
    """Cache item (internal)."""

    data: Any
    node: _ListNode


class LruCache(MutableMapping, contextlib.AbstractContextManager):
    """Lru cache (thread-safe).

    Synchronization is performed internally with a reentrant lock.
    Manual synchronization with context protocol or acquire/release methods
    is needed only to implement the atomic operations.
    """

    def __init__(self, maxsize=128):
        """Create a new cache instance limited by maxsize items."""
        self._lock = threading.RLock()
        self._cache: dict[Any, _CacheItem] = {}
        self._list = _LinkedList()
        self._maxsize: Final = maxsize
        self._hits = 0
        self._misses = 0

    def __getitem__(self, key: Any) -> Any:
        """Return an item with the specified key."""
        with self._lock:
            try:
                item = self._cache[key]
                data, node = item.data, item.node
                self._hits += 1
            except KeyError:
                self._misses += 1
                raise
            self._list.touch(node)
            return data

    def __setitem__(self, key: Any, value: Any) -> None:
        """Set the item at the specified key."""
        with self._lock:
            if key in self._cache:
                item = self._cache[key]
                item.data = value
                self._list.touch(item.node)
                return
            # not exists
            node = self._list.appendleft(key)
            self._cache[key] = _CacheItem(value, node)
            if len(self._cache) > self._maxsize:
                node = self._list.pop()
                self._cache.pop(node.data)

    def __delitem__(self, key: Any) -> None:
        """Delete the item at the specified key."""
        with self._lock:
            item = self._cache.pop(key)
            self._list.pop(item.node)
            return item.data

    def __iter__(self) -> Iterator[Any]:
        """Iterate over the cache keys in the first-used order."""
        with self._lock:
            for node in self._list:
                yield node.data

    def __len__(self) -> int:
        """Return the cache length."""
        with self._lock:
            assert len(self._cache) == len(
                self._list
            ), "Table and tracker are out of sync"
            return len(self._cache)

    def __enter__(self) -> Self:
        """Acquire the cache lock."""
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Release the cache lock."""
        self._lock.release()
        return False  # re-raise exception (if any)

    def keys(self) -> Iterator[Any]:
        """Return an iterator over the cache keys in the first-used order."""
        return iter(self)

    def values(self) -> Iterator[Any]:
        """Return an iterator over the cache values in the first-used order."""
        with self._lock:
            for node in self._list:
                key = node.data
                yield self._cache[key].data

    def items(self) -> Iterator[tuple[Any, Any]]:
        """Return an iterator over the cache key/value pairs in the first-used order."""
        with self._lock:
            for node in self._list:
                key = node.data
                yield key, self._cache[key].data

    def clear(self):
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
