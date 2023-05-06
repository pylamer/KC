from itertools import cycle

from b2b_scoring import load_balancing

# Инициализируется в __init__
redis_connection = None


def discover(service_name: str):
    def wrapped_discover():
        replicas_pool = []
        print(service_name)
        service_replicas: list = redis_connection.lrange(service_name, 0, -1)
        for replica in service_replicas:
            host, port = redis_connection.hmget(replica, keys=['host', 'port'])
            if (host is None) and (port is None):
                # Реплика недоступна
                # TODO: Удалить ее из списка и удалить ее из реджистри
                pass
            elif (host is not None) and (port is not None):
                # Реплика доступна. Добавим его в пул
                replicas_pool.append(tuple([replica, host, port]))
            else:
                # Неопределенное поеведение
                raise RuntimeError
        load_balancing.replicas_pool = cycle(replicas_pool)
        print(replicas_pool)
    return wrapped_discover
