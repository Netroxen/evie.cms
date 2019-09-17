# -*- coding: utf-8 -*-

from quart import Blueprint, render_template
from evie.forms.auth import LoginForm

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=('GET', 'POST'))
@bp.route('/<path:came_from>/login', methods=('GET', 'POST'))
async def login(came_from=''):
    form = LoginForm()
    return await render_template('auth/login.html.j2', form=form)
