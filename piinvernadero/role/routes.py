from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from piinvernadero import db
from piinvernadero.role import bp
from piinvernadero.role.forms import RoleCreateForm
from piinvernadero.models import Role

@bp.route('/create', methods=['GET', 'POST'])
def createrole():
    #if current_user.is_authenticated: # Si no es admin
    #    return redirect(url_for('main.index'))
    form = RoleCreateForm()
    #if form.validate_on_submit():
        #role = Role(name=form.name.data, description=form.description.data)
        #role.set_name(form.name.data)
        #role.set_description(form.description.data)
        #db.session.add(role)
        #db.session.commit()
        #flash(_('Role created!'))
        #return redirect(url_for('role.create'))
    return render_template('role/create.html', title=_('Create'), form=form)
    
