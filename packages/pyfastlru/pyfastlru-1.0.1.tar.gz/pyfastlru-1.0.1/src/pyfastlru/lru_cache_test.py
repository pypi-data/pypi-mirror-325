# pyfastlru v. 1.0
# Thread-safe LRU cache with the MutableMapping interface.
# SPDX-FileCopyrightText: Copyright © 2025 Anatoly Petrov <petrov.projects@gmail.com>
# SPDX-License-Identifier: MIT

"""Lru cache tests (pytest framework)."""

import dataclasses
from typing import Any
import warnings

try:
    import pytest

    _NO_PYTEST = False
except ModuleNotFoundError:
    _NO_PYTEST = True
    warnings.warn(
        "The pytest framework is not available. "
        "Tests will be executed without any framework support."
    )

import lru_cache


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


@dataclasses.dataclass
class _CacheInfo:
    """Modifiable cache info."""

    hits: int = 0
    misses: int = 0
    maxsize: int = 0
    currsize: int = 0

    def __eq__(self, other):
        return (
            self.hits == other.hits
            and self.misses == other.misses
            and self.maxsize == other.maxsize
            and self.currsize == other.currsize
        )


def _check_node(
    node: lru_cache._ListNode,
    prev: lru_cache._ListNode | None,
    next: lru_cache._ListNode | None,
    data: Any,
) -> None:
    """Check list node (internal)."""
    assert node.prev is prev
    assert node.next is next
    assert node.data is data


def _check_list(
    seq: lru_cache._LinkedList,
    content: list,
    front: lru_cache._ListNode | None,
    back: lru_cache._ListNode | None,
    size: int,
    empty: bool = False,
) -> None:
    """Check linked list (internal)."""
    assert [node.data for node in seq] == content
    if front is not None:
        assert seq.front is front
    if back is not None:
        assert seq.back is back
    assert len(seq) == size
    assert not bool(seq) == empty


def _check_cache(
    cache: lru_cache.LruCache,
    items: list,
    size: int,
    empty: bool = False,
    stats: _CacheInfo | None = None,
):
    """Check cache (end-user api testing)."""
    assert list(cache.items()) == items
    assert len(cache) == size
    assert not bool(cache) == empty
    assert cache.cache_info() == stats


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


class TestLruCache:
    """Tests for lru cache (end-user) and linked list (aux)."""

    def test_aux_linked_list(self):
        """Test internal linked list implementation."""
        # init()
        seq = lru_cache._LinkedList()
        _check_list(seq, content=[], front=None, back=None, size=0, empty=True)
        # appendleft()
        a = seq.appendleft("a")
        _check_node(a, prev=None, next=None, data="a")
        _check_list(seq, content=["a"], front=a, back=a, size=1)
        b = seq.appendleft("b")
        _check_node(b, prev=None, next=a, data="b")
        _check_list(seq, content=["b", "a"], front=b, back=a, size=2)
        c = seq.appendleft("c")
        _check_node(c, prev=None, next=b, data="c")
        _check_list(seq, content=["c", "b", "a"], front=c, back=a, size=3)
        # touch()
        seq.touch(a)
        _check_node(a, prev=None, next=c, data="a")
        _check_list(seq, content=["a", "c", "b"], front=a, back=b, size=3)
        seq.touch(c)
        _check_node(c, prev=None, next=a, data="c")
        _check_list(seq, content=["c", "a", "b"], front=c, back=b, size=3)
        seq.touch(c)
        _check_node(c, prev=None, next=a, data="c")
        _check_list(seq, content=["c", "a", "b"], front=c, back=b, size=3)
        # pop()
        removed = seq.pop()
        assert removed is b
        _check_node(a, prev=c, next=None, data="a")
        _check_list(seq, content=["c", "a"], front=c, back=a, size=2)
        removed = seq.pop()
        assert removed is a
        _check_node(c, prev=None, next=None, data="c")
        _check_list(seq, content=["c"], front=c, back=c, size=1)
        removed = seq.pop()
        assert removed is c
        _check_list(seq, content=[], front=None, back=None, size=0, empty=True)
        # clear()
        seq.appendleft("a")
        seq.appendleft("b")
        seq.appendleft("c")
        seq.clear()
        _check_list(seq, content=[], front=None, back=None, size=0, empty=True)

    def test_lru_cache(self):
        """Test lru cache end-user api."""
        # init()
        cache = lru_cache.LruCache(maxsize=3)
        stats = _CacheInfo(maxsize=3)
        _check_cache(cache, items=[], size=0, empty=True, stats=stats)
        # setitem()
        cache[0] = "a"
        stats.currsize += 1
        _check_cache(cache, items=[(0, "a")], size=1, stats=stats)
        cache[1] = "b"
        stats.currsize += 1
        _check_cache(cache, items=[(1, "b"), (0, "a")], size=2, stats=stats)
        cache[2] = "c"
        stats.currsize += 1
        _check_cache(cache, items=[(2, "c"), (1, "b"), (0, "a")], size=3, stats=stats)
        # getitem()
        assert cache[2] == "c"
        stats.hits += 1
        _check_cache(cache, items=[(2, "c"), (1, "b"), (0, "a")], size=3, stats=stats)
        assert cache[1] == "b"
        stats.hits += 1
        _check_cache(cache, items=[(1, "b"), (2, "c"), (0, "a")], size=3, stats=stats)
        assert cache[0] == "a"
        stats.hits += 1
        _check_cache(cache, items=[(0, "a"), (1, "b"), (2, "c")], size=3, stats=stats)
        assert cache.get(3, None) is None
        stats.misses += 1
        _check_cache(cache, items=[(0, "a"), (1, "b"), (2, "c")], size=3, stats=stats)
        # delitem()
        del cache[1]
        stats.currsize -= 1
        _check_cache(cache, items=[(0, "a"), (2, "c")], size=2, stats=stats)
        assert cache.pop(2) == "c"
        stats.currsize -= 1
        stats.hits += 1
        _check_cache(cache, items=[(0, "a")], size=1, stats=stats)
        assert cache.popitem() == (0, "a")
        stats.currsize -= 1
        stats.hits += 1
        _check_cache(cache, items=[], size=0, empty=True, stats=stats)
        # item replacement
        cache = lru_cache.LruCache(maxsize=3)
        stats = _CacheInfo(maxsize=3)
        cache.update({1: "a", 2: "b", 3: "c"})
        stats.currsize += 3
        cache[1] = "x"
        _check_cache(cache, items=[(1, "x"), (3, "c"), (2, "b")], size=3, stats=stats)
        cache[2] = "y"
        _check_cache(cache, items=[(2, "y"), (1, "x"), (3, "c")], size=3, stats=stats)
        cache[3] = "z"
        _check_cache(cache, items=[(3, "z"), (2, "y"), (1, "x")], size=3, stats=stats)
        # cache bound
        cache = lru_cache.LruCache(maxsize=3)
        stats = _CacheInfo(maxsize=3)
        cache.update({1: "a", 2: "b", 3: "c"})
        stats.currsize += 3
        _check_cache(cache, items=[(3, "c"), (2, "b"), (1, "a")], size=3, stats=stats)
        cache[4] = "d"
        _check_cache(cache, items=[(4, "d"), (3, "c"), (2, "b")], size=3, stats=stats)
        assert cache[2] == "b"
        stats.hits += 1
        _check_cache(cache, items=[(2, "b"), (4, "d"), (3, "c")], size=3, stats=stats)
        cache[5] = "e"
        _check_cache(cache, items=[(5, "e"), (2, "b"), (4, "d")], size=3, stats=stats)
        assert cache[4] == "d"
        stats.hits += 1
        _check_cache(cache, items=[(4, "d"), (5, "e"), (2, "b")], size=3, stats=stats)
        cache[6] = "f"
        _check_cache(cache, items=[(6, "f"), (4, "d"), (5, "e")], size=3, stats=stats)
        # clear()
        cache.clear()
        stats = _CacheInfo(maxsize=3)
        _check_cache(cache, items=[], size=0, empty=True, stats=stats)


if _NO_PYTEST:

    def launch_tests():
        suite = TestLruCache()
        suite.test_aux_linked_list()
        suite.test_lru_cache()

    if __name__ == "__main__":
        launch_tests()
