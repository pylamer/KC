from flask import Blueprint

from b2b_scoring.load_balancing import round_robin


bp = Blueprint(name='client-side-load-balancing',
               import_name=__name__,
               url_prefix='/c-s-l-b')


@bp.route('/')
def handler():
    next_in_pool = round_robin()
    return next_in_pool.__str__()
