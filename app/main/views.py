from flask import render_template,redirect,url_for,abort,flash,request
from app import db
from . import main
from flask_login import login_required,current_user
from ..models import User,BlogPost,Comment,Role
from .forms import UpdateProfile,CommentForm,PostForm
from .picture_handler import add_profile_pic


#views
@main.route('/')
def index():
    '''
    view root function that returns index page and its data
    '''
    return render_template('index.html',title='Home of the brave')


@main.route('/user/<uname>/profile_update',methods=['GET','POST'])
@login_required
def profile_update(uname):
    '''
    view function to updtae a user profile
    '''
    form=UpdateProfile()
    if form.validate_on_submit():

        if form.pictures.data:
            username=current_user.username
            pic=add_profile_pic(form.pictures.data,username)

            #setting current user image to the new uploaded pic
            current_user.profile_image=pic

        #resetting user data
        current_user.username=form.username.data
        current_user.email=form.email.data 
        db.session.commit()  
        flash('Account Updated')
        return redirect(url_for('.profile'))

    elif request.method=='GET':
        #user is not submitting anything
        form.username.data=current_user.username
        form.email.data=current_user.email
    
    #fetch the current profile image from the static folder and inject to the template    
    profile_image=url_for('static',filename='photos/'+current_user.profile_image)  
    return render_template('profile.html',profile_image=profile_image,form=form)  


