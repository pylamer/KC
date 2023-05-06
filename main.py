import os
import time
import random
import json
from flask import Flask, request, jsonify
from utils import get_secret_number
import redis
# from b2b_scoring import init_redis, init_scheduler, views

URL_SEC_NUMBER = 'https://lab.karpov.courses/hardml-api/module-5/get_secret_number'
secret_number = get_secret_number(URL_SEC_NUMBER)

app = Flask(__name__)

@app.route('/return_secret_number')
def return_secret_number():
    return jsonify(secret_number=secret_number)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

    app_name = "web_app"
    replic_name = "replic1"
    host_name = "95.216.191.176"
    port_name = 5000

    # redis_client = redis.Redis(host="localhost", port=6379, db=0, password='lolkek123')
    redis_client = redis.Redis(host="172.17.0.2", port=6379, db=0, password='lolkek123')
    redis_client.rpush(app_name, replic_name)

    redis_client.hset(replic_name, "host", host_name)
    redis_client.hset(replic_name, "port", port_name)

    redis_client.close()


