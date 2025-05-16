from flask import Blueprint

optimization_route =  Blueprint('optimization', __name__)


@optimization_route.route("simplex")
def simplex():
    pass

@optimization_route.route("dual_simplex")
def dual_simplex():
    pass

@optimization_route.route("branch_and_bound")
def branch_and_bound():
    pass