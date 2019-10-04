# -*- coding: utf-8 -*-

from quart import Blueprint, render_template

bp = Blueprint('base', __name__)


@bp.route('/')
async def index():
    return await render_template('base/base.html.j2')
