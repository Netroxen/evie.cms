# -*- coding: utf-8 -*-

from flask_login import login_required, login_user, logout_user
from quart import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)

from evie.forms.auth import LoginForm, RegistrationForm

bp = Blueprint('auth', __name__)


@bp.route('/login', methods=('GET', 'POST'))
async def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = current_app.get_user(form.username.data)
        if user.check_password(form.password.data):
            login_user(user)
            await flash('Logged in successfully.', 'primary')
            return redirect(url_for(request.args.get('next', 'base.index')))
    return await render_template('auth/login.html.j2', form=form)


@bp.route('/logout', methods=('GET', 'POST'))
@login_required
async def logout():
    logout_user()
    return redirect(url_for(request.args.get('next', 'auth.login')))


@bp.route('/register', methods=('GET', 'POST'))
async def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            current_app.create_user(
                form.email.data,
                form.password.data,
                form.username.data,
            )
            await flash('Account successfully registered.', 'success')
            return redirect(url_for(request.args.get('next', 'auth.login')))
        except KeyError:
            await flash('The account could not be registered.', 'danger')
            return redirect(url_for(request.args.get('next', 'auth.register')))
    return await render_template('auth/register.html.j2', form=form)
