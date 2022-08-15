import redis
import random

with redis.Redis() as redis_server:
    redis_server.rpush("queue", random.randint(0, 999))

