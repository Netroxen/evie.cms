# -*- coding: utf-8 -*-

from jinja2 import TemplateNotFound
from quart import Blueprint, abort, render_template

bp = Blueprint('public', __name__)


@bp.route('/')
async def index():
    return await render_template(f'public/index.j2.html')
