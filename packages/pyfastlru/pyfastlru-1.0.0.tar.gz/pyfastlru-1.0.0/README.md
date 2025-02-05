# pyfastlru v. 1.0

**Python implementation of a thread-safe LRU cache.**

Features: thread safety, statistics, familiar interface.

The MIT License (MIT). Copyright © 2025 Anatoly Petrov <petrov.projects@gmail.com>

# Description

LRU cache is a data structure that combines fast item access by the key with 
invalidation of least recently used items in case of size limit exhaustion.

These traits make the LRU cache useful for memoizing some computations 
(requests, resources, etc.) without risking memory blowup.

Our implementation uses a doubly linked list for item usage tracking and a `dict` 
for the lookup table.

# Overview

The cache provides a `MutableMapping` interface. Thus, you may use `LruCache` 
the same way you use `dict`. 

Unlike the standard `dict` (which is unbounded), the cache size is limited 
by the `maxsize` value provided to the cache `__init__` method (`128` by default). 
If the item count exceeds the limit,`LruCache` automatically removes the least recently used item.

Synchronization is performed internally by the cache with a reentrant lock and doesn't require
any actions from the end-user.

Manual synchronization with `LruCache` context protocol or `acquire`/`release` methods 
is needed only to implement the atomic operations.

Cache collects usage statistics (`hits`, `misses`, `maxsize`, `currsize`) 
which may be retrieved with the `cache_info()` method.

# Testing

`pyfastlru` is tested with `pytest` framework.

# License

`pyfastlru` is licensed under the MIT License, see [LICENSE](LICENSE) for more information.
