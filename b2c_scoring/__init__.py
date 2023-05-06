import redis

from b2b_scoring import service_discover

from flask_apscheduler import APScheduler


def init_redis(host: str, port: int):
    if service_discover.redis_connection is None:
        # Еще не создан - создайте
        service_discover.redis_connection = redis.Redis(host=host, port=port, decode_responses=True)
    else:
        # Коннект уже почему то создан
        pass


def init_scheduler(service_name: str):
    service_discover.discover(service_name=service_name)
    scheduler = APScheduler()
    scheduler.add_job(id='kek',
                      func=service_discover.discover(service_name=service_name),
                      trigger='interval', seconds=5)
    return scheduler

