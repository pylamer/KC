import os
import time
import random

from flask import Flask
from flask import request
from utils import get_secret_number

from b2b_scoring import init_redis, init_scheduler, views

app = Flask(__name__)

@app.route('/return_secret_number')
def return_secret_number():
    print(request)
    time.sleep(random.random()*4)
    pid = os.getpid()
    return 'Hello World! ' + pid.__str__()


if __name__ == '__main__':

    # init_redis(host='192.168.1.10', port=6379)
    init_redis(host='192.168.1.146', port=6379)

    scheduler = init_scheduler(service_name='service_b')
    scheduler.init_app(app)
    scheduler.start()

    app.register_blueprint(views.bp)

    app.run()

    a = "dasdasdas" \
        "asdasda"