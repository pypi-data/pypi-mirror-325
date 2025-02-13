# pyfastlru v. 1.0

**Python implementation of a thread-safe LRU cache.**

Features: thread safety, statistics, familiar interface.

The MIT License (MIT). Copyright © 2025 Anatoly Petrov <petrov.projects@gmail.com>

# Description

An LRU (Least Recently Used) cache is a data structure that provides quick access 
to items by key and automatically removes the least recently used items in case of 
size exhaustion.

These characteristics make the LRU cache ideal for memoizing arbitrary data 
without the risk of excessive memory usage. 

The proposed implementation (`LruCache` class) utilizes a doubly linked list 
to track item usage and a dictionary for the lookup table.

# Overview

The `LruCache` provides a `MutableMapping` interface similar to the `dict`.

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

# Testing

`pyfastlru` is tested with `pytest` framework.

# License

`pyfastlru` is licensed under the MIT License, see [LICENSE](LICENSE) for more information.
