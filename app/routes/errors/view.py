from flask import render_template

from app.routes.errors import bp


@bp.app_errorhandler(401)
def unreg(error):
    return "Test 401", 401


@bp.app_errorhandler(404)
def page_is_not_found(error):
    return "Test 404", 404