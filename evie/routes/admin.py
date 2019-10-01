# -*- coding: utf-8 -*-

from flask_login import current_user
from quart import Blueprint, redirect, render_template, url_for

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.before_request
async def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
