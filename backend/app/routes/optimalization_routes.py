from flask import Blueprint

optimization_route =  Blueprint('optimizarion', __name__)


@optimization_route.route("simplex")
def simplex():
    pass