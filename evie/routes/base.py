# -*- coding: utf-8 -*-

from quart import Blueprint, render_template, current_app

bp = Blueprint('base', __name__)


@bp.route('/')
async def index():
    site = current_app.get_site()
    return await render_template('base/index.html.j2', site=site)
