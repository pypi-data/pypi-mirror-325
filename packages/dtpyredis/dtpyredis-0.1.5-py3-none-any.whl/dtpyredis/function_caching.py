import base64
import hashlib
import json
import logging
import zlib
from functools import wraps
from dtpyutils import jsonable_encoder
from dtpyutils.exception import exception_to_dict, RequestException
from dtpyredis.connection import RedisInstance


def hash_data(data):
    prepared_data = base64.b64encode(json.dumps(jsonable_encoder(data), sort_keys=True).encode('utf8')).decode('utf-8')
    data = str(prepared_data)
    return f"{hashlib.sha256(data.encode()).hexdigest()}{len(data)}"


def get_cached_data(redis_instance, redis_key):
    try:
        return redis_instance.get(redis_key)
    except Exception as exception:
        logging.error(
            msg='We faced an error while we want to get a cache.',
            extra=dict(
                controller='caching.get_cached_data',
                subject='Error on get cached data',
                payload={
                    'redis_key': redis_key,
                    'error': exception_to_dict(exception),
                }
            )
        )

    return None


def cache_data(response, expire, redis_instance, cache_key):
    try:
        compressed_main_value = zlib.compress(json.dumps(jsonable_encoder(response)).encode('utf-8'))
        redis_instance.delete(cache_key)
        if expire:
            redis_instance.setex(name=cache_key, value=compressed_main_value, time=expire)
        else:
            redis_instance.set(name=cache_key, value=compressed_main_value)

    except Exception as exception:
        logging.error(
            msg='We faced an error while we want to cache data.',
            extra=dict(
                controller='caching.cache_data',
                subject='Error on caching data',
                payload={
                    'expire': expire,
                    'cache_key': cache_key,
                    'error': exception_to_dict(exception),
                }
            )
        )

    return response


def get_data_from_source(func, *args, **kwargs):
    try:
        should_cache, result = True, func(*args, **kwargs)
    except RequestException as e:
        raise e
    except Exception as e:
        logging.error(
            msg='We faced an error while we want to run a function.',
            extra=dict(
                controller='cache.get_data_from_source',
                subject='Error on running a function',
                payload=exception_to_dict(e)
            )
        )
        raise e
    else:
        return should_cache, result


def cache_function(
        redis: RedisInstance,
        namespace: str,
        expire: int | None = None,
        in_route_arguments: set[str] | list[str] | None = None,
        body_arguments: set[str] | list[str] | None = None,
):
    if not in_route_arguments:
        in_route_arguments = []

    if not body_arguments:
        body_arguments = []

    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            site_url: str = kwargs.get('site_url')

            if site_url:
                site_url = site_url[4:] if site_url and site_url.startswith("www.") else site_url
                cache_key = f"websites-caches:{site_url}:"
            else:
                cache_key = 'functions-caches:'

            cache_key += namespace
            for key in in_route_arguments:
                cache_key += f':{str(kwargs.get(key) or None).replace(":", "-")}'

            request_hashable_data = {}
            if body_arguments:
                request_hashable_data.update({
                    k: v for k, v in kwargs.items()
                    if k in body_arguments
                })

            if request_hashable_data:
                plus_cache_key = hash_data(request_hashable_data)
                cache_key += f":{plus_cache_key}"

            with redis.get_redis_client() as redis_instance:
                cache_compressed = get_cached_data(redis_instance=redis_instance, redis_key=f"{cache_key}")
                if cache_compressed is None:
                    should_cache, response = get_data_from_source(func, *args, **kwargs)
                    if should_cache:
                        return cache_data(
                            response=response,
                            expire=expire,
                            redis_instance=redis_instance,
                            cache_key=cache_key,
                        )
                    else:
                        return response

                try:
                    return json.loads(zlib.decompress(cache_compressed).decode('utf-8'))
                except Exception as exception:
                    logging.error(
                        msg='We faced an error while we want to read a cache.',
                        extra=dict(
                            controller='caching.cache',
                            subject='Error on reading cache',
                            message='We faced an error while we want to read a cache.',
                            payload=exception_to_dict(exception)
                        )
                    )
                    should_cache, response = get_data_from_source(func, *args, **kwargs)
                    if should_cache:
                        return cache_data(
                            response=response,
                            expire=expire,
                            redis_instance=redis_instance,
                            cache_key=cache_key,
                        )
                    else:
                        return response

        return wrapper

    return decorator
