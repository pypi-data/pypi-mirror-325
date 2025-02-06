.. _aiohttp_asyncmdnsresolver-api:

=========
Reference
=========

.. module:: aiohttp_asyncmdnsresolver.api

The only public *aiohttp_asyncmdnsresolver.api* classes are :class:`AsyncMDNSResolver`
and :class:`AsyncDualMDNSResolver`:

.. doctest::

   >>> from aiohttp_asyncmdnsresolver.api import AsyncMDNSResolver


.. class:: AsyncMDNSResolver(*args, *, async_zeroconf=None, mdns_timeout=5.0, **kwargs)

   This class functions the same as ``aiohttp.resolver.AsyncResolver``,
   but with the added ability to resolve mDNS queries.

    :param ``AsyncZeroconf`` async_zeroconf: If an ``AsyncZeroconf`` instance is
        passed, it will be used to resolve mDNS queries. If not, a new
        instance will be created.

    :param float mdns_timeout: The timeout for the mDNS query in seconds. If not provided
        the default timeout is 5 seconds. If the mdns_timeout is set to 0, the
        query will only use the cache and will not perform a new query.

   Example::

       from aiohttp_asyncmdnsresolver.api import AsyncMDNSResolver

       resolver = AsyncMDNSResolver()
       connector = aiohttp.TCPConnector(resolver=resolver)
       async with aiohttp.ClientSession(connector=connector) as session:
           async with session.get("http://KNKSADE41945.local.") as response:
               print(response.status)


.. class:: AsyncDualMDNSResolver(*args, *, async_zeroconf=None, mdns_timeout=5.0, **kwargs)

   This resolver is a variant of :class:`AsyncMDNSResolver` that resolves ``.local``
    names with both mDNS and regular DNS. It takes the same arguments as
    :class:`AsyncMDNSResolver`, and is used in the same way.

   - The first successful result from either resolver is returned.
   - If both resolvers fail, an exception is raised.
   - If both resolvers return results at the same time, the results are
     combined and duplicates are removed.
