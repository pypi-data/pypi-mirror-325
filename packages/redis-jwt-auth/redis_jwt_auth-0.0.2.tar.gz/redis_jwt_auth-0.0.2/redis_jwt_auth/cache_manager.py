import redis
import json


class CacheManager:
    def __init__(self, redis_host: str = "localhost", redis_port: int = 6379, db: int = 0):
        self.redis = redis.Redis(host=redis_host, port=redis_port, db=db, decode_responses=True)

    def store_tokens(self, user_id, access_jti, refresh_jti, expiry):
        self.redis.setex(f"token:{user_id}", expiry, json.dumps({"access_jti": access_jti, "refresh_jti": refresh_jti}))

    def get_tokens(self, user_id):
        data = self.redis.get(f"token:{user_id}")
        return json.loads(data) if data else None

    def delete_tokens(self, user_id):
        self.redis.delete(f"token:{user_id}")

    def store_user_object(self, user_id, user_data, expiry):
        self.redis.setex(f"user:{user_id}", expiry, json.dumps(user_data))

    def get_user_object(self, user_id):
        data = self.redis.get(f"user:{user_id}")
        return json.loads(data) if data else None

    def delete_user_object(self, user_id):
        self.redis.delete(f"user:{user_id}")