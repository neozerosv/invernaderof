from flask import render_template
from piinvernadero import piinvernadero
from piinvernadero.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from piinvernadero.models import User
from piinvernadero import db
from piinvernadero.forms import RegistrationForm
from datetime import datetime
from piinvernadero.forms import EditProfileForm
from flask_babel import _

@piinvernadero.route('/')
@piinvernadero.route('/index')
@login_required
def index(): 
    posts =  [{"mensaje":"Hola mundo!!"}, {"mensaje":"Aca en.."}]
    return render_template("index.html", title=_('Home Page'), posts=posts)    


@piinvernadero.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()    
    return render_template('user/user.html', user=user)

@piinvernadero.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@piinvernadero.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('user/edit_profile.html', title=_('Edit Profile'), form=form)