import random
import socket

from flask import Flask
from flask import request

from prometheus_flask_exporter import PrometheusMetrics

INT = random.randint(1, 100)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_int', 'Application info', version=INT)

PORT = 6000


def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

print("PORT1: ", PORT),
print(is_port_in_use(PORT))
while not is_port_in_use(PORT):
    PORT = PORT + 1
print("PORT: ", PORT)

@app.route('/')
def hello_world():
    print(request)
    return 'Kek'


if __name__ == '__main__':
    app.run(port=PORT)

