import redis
import random

with redis.Redis() as redis_client:
    value = redis_client.brpop("queue")


print(int(value[1]))