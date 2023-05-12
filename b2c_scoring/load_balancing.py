from itertools import cycle

replicas_pool = cycle([])


def round_robin():
    return next(replicas_pool)


def load_balancing_algo_2():
    return next(replicas_pool)


def load_balancing_algo_3():
    return next(replicas_pool)
