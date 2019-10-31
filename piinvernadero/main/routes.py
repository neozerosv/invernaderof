from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
#from guess_language import guess_language
from piinvernadero import db
from piinvernadero.main.forms import EditProfileForm
# PostForm
from piinvernadero.models import User
#from piinvernadero.translate import translate
from piinvernadero.main import bp


@bp.route('/')
@bp.route('/index')
@login_required
def index(): 
    posts =  [{"mensaje":"Hola mundo!!"}, {"mensaje":"Aca en.."}]
    return render_template("index.html", title=_('Home Page'), posts=posts)    


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()    
    return render_template('user/user.html', user=user)

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data        
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name

    return render_template('user/edit_profile.html', title=_('Edit Profile'), form=form)