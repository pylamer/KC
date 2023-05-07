import os
import random
from flask import Flask, request, jsonify
from utils import get_secret_number
import redis
import signal
import sys
import json
import time

# from b2b_scoring import init_redis, init_scheduler, views

URL_SEC_NUMBER = 'https://lab.karpov.courses/hardml-api/module-5/get_secret_number'
port = os.environ.get("FLASK_PORT")
# port = "5004"
print('flask port', port)
host_name = "95.216.191.176"
app_name = "web_app"
replic_name = "_".join([app_name, host_name, port])

def handler(sig, frame):
    handler_redis_client = redis.Redis(host="172.17.0.2", port=6379, db=0, password='lolkek123')
    handler_redis_client.lrem(app_name, 0, replic_name)
    handler_redis_client.delete(replic_name)
    sys.exit(0)

signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)

app = Flask(__name__)

@app.route('/return_secret_number')
def return_secret_number():
    return jsonify(secret_number=secret_number, random_number=random.randint(1, 10))

if __name__ == '__main__':
    secret_number = get_secret_number(URL_SEC_NUMBER)

    # redis_client = redis.Redis(host="localhost", port=6379, db=0, password='lolkek123')
    redis_client = redis.Redis(host="172.17.0.2", port=6379, db=0, password='lolkek123')
    redis_client.rpush(app_name, replic_name)

    redis_client.hset(replic_name, "host", host_name)
    redis_client.hset(replic_name, "port", port)

    redis_client.close()

    app.run(host="0.0.0.0", port=port)
