# -*- coding: utf-8 -*-

from quart import Blueprint, render_template

bp = Blueprint('errors', __name__)


@bp.app_errorhandler(404)
async def handle_404(e):
    return await render_template('errors/404.j2.html', title='404'), 404


@bp.app_errorhandler(500)
async def handle_500(e):
    return await render_template('errors/500.j2.html', title='500'), 500
