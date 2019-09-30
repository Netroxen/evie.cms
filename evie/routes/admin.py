# -*- coding: utf-8 -*-

from quart import Blueprint, render_template

bp = Blueprint('admin', __name__)


async def setup():
    return await render_template('base/setup.html.j2')
