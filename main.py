import os
import time
import random
import json
from flask import Flask, request, jsonify
from utils import get_secret_number
# from b2b_scoring import init_redis, init_scheduler, views

URL_SEC_NUMBER = 'https://lab.karpov.courses/hardml-api/module-5/get_secret_number'

app = Flask(__name__)

@app.route('/return_secret_number')
def return_secret_number():
    secret_number = get_secret_number(URL_SEC_NUMBER)
    return jsonify(secret_number=secret_number)


if __name__ == '__main__':

    # init_redis(host='192.168.1.10', port=6379)
    # init_redis(host='192.168.1.146', port=6379)
    #
    # scheduler = init_scheduler(service_name='service_b')
    # scheduler.init_app(app)
    # scheduler.start()
    #
    # app.register_blueprint(views.bp)

    app.run(host="0.0.0.0", port=5000)