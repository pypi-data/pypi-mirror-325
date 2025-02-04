import os

from requests_cache import CachedSession, RedisCache, SQLiteCache

if os.environ.get("REQUEST_CACHE") == "redis":
    host = os.environ.get("REQUEST_CACHE_HOST", "redis")
    port = os.environ.get("REQUEST_CACHE_PORT", 6379)
    password = os.environ.get("REQUEST_CACHE_PASSWORD", None)
    ttl_offset = os.environ.get("REQUEST_CACHE_TTL", 3600)

    print("Using redis for cache backend")
    backend = RedisCache(
        host="redis", port=port, ttl_offset=ttl_offset, password=password
    )
else:
    print("Using sqlite for cache backend")
    path = os.environ.get("REQUEST_CACHE_PATH", "cache/http_cache.sqlite")
    wal = os.environ.get("REQUEST_CACHE_WAL", True)
    backend = SQLiteCache(path, wal=wal)

session = CachedSession(
    "demo_cache",
    use_cache_dir=True,  # Save files in the default user cache dir
    cache_control=True,  # Use Cache-Control response headers for expiration, if available
    expire_after=int(
        os.environ.get("REQUEST_CACHE_EXPIRY_AFTER", 120)
    ),  # Otherwise expire responses after one day
    allowable_codes=[
        200,
    ],
    match_headers=["Accept-Language"],  # Cache a different response per language
    stale_if_error=True,  # In case of request errors, use stale cache data if possible
    backend=backend,
)
