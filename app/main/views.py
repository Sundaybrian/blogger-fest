from flask import render_template,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,BlogPost,Comment,Role


#views
@main.route('/')
def index():
    '''
    view root function that returns index page and its data
    '''
    return render_template('index.html',title='Home of the brave')
