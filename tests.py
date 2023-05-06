import redis

app_name = "web_app"
replic_name = "replic1"
host_name = "95.216.191.176"
port_name = 5000

redis_client = redis.Redis(host="localhost", port=6379, db=0, password='lolkek123')
redis_client.rpush(app_name, replic_name)

redis_client.hset(replic_name, "host", host_name)
redis_client.hset(replic_name, "port", port_name)

redis_client.close()
