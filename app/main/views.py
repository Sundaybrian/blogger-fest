from flask import render_template,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,BlogPost,Comment,Role
from .forms import UpdateProfile,CommentForm,PostForm


#views
@main.route('/')
def index():
    '''
    view root function that returns index page and its data
    '''
    return render_template('index.html',title='Home of the brave')


@main.route('/profile',methods=['GET','POST'])
def profile(uname):
    '''
    view function for a user profile
    '''
    form=UpdateProfile()
    if form.validate_on_submit():
        
    user=User.query.filter_by(username=uname).first()
