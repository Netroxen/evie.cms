# -*- coding: utf-8 -*-

from quart import Blueprint, render_template

bp = Blueprint('errors', __name__)


@bp.app_errorhandler(403)
async def handle_403(e):
    return await render_template('errors/403.html.j2'), 403


@bp.app_errorhandler(404)
async def handle_404(e):
    return await render_template('errors/404.html.j2'), 404


@bp.app_errorhandler(405)
async def handle_405(e):
    return await render_template('errors/405.html.j2'), 405


@bp.app_errorhandler(500)
async def handle_500(e):
    return await render_template('errors/500.html.j2'), 500
