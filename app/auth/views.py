from flask import render_template,redirect,url_for,request,
from . import auth
from app.models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,login_required,logout_user

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user.verify_password(form.password.data) and user is not None:
            login_user(user,form.remember.data)
            flash('Log in Success')
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Username or Password')
    
    title='BlogFest Login'
    return render_template('auth/login.html',form=form,title=title)    