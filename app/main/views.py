from flask import render_template,redirect,url_for,abort,flash,request
from app import db
from . import main
from flask_login import login_required,current_user
from ..models import User,BlogPost,Comment,Role
from .forms import UpdateProfileForm,CommentForm,PostForm
from .picture_handler import add_profile_pic


#views
@main.route('/')
def index():
    '''
    view root function that returns index page and its data
    '''
    posts=BlogPost.query.all()
    return render_template('index.html',title='Home of the brave',posts=posts,user=current_user)



@main.route('/user/<uname>')
def profile(uname):
    '''
    view function to see a single user profile
    '''
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user=user)

    
@main.route('/user/<uname>/profile_update',methods=['GET','POST'])
@login_required
def profile_update(uname):
    '''
    view function to updtae a user profile
    '''
    form=UpdateProfileForm()
    if form.validate_on_submit():

        if form.pictures.data:
            # uname=current_user.username
            pic=add_profile_pic(form.pictures.data,uname)

            #setting current user image to the new uploaded pic
            
            current_user.profile_image=pic
            
            

        #resetting user data
        current_user.username=form.username.data
        current_user.email=form.email.data 
        db.session.commit() 

        flash('Account Updated')
        return redirect(url_for('main.profile',uname=current_user.username))

    elif request.method=='GET':
        #user is not submitting anything
        #leave the form values as they are
        form.username.data=current_user.username
        form.email.data=current_user.email
    
    #fetch the current profile image from the static folder and inject to the template    
    profile_image=url_for('static',filename='photos/'+current_user.profile_image)  
    return render_template('profile/update_profile.html',profile_image=profile_image,form=form)  


@main.route('/<uname>/blogposts')
def user_posts(uname):
    '''
    View function that displays all blog posts for a single user
    '''
    #cycle through user posts using pages e.g if user has 40 posts we dont display all in one page
    page=request.args.get('page',1,type=int)

    #grab user if he/she exists or return 404
    user=User.query.filter_by(uname=uname).first_or_404()

    #grab posts by the specified user 
    posts=BlogPost.get_user_posts(user ,page)

    title=f'{uname}-blogposts'
    return render_template('user_blogposts.html',posts=posts,user=user,title=title)


@main.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    '''
    View function to create a blog post
    '''
    form=PostForm()

    if form.validate_on_submit():
        post=BlogPost(title=form.title.data,text=form.text.data,user_id=current_user.id)

        post.save_post()
        flash('Blog Post Created')
        return redirect(url_for('main.index'))

    return render_template('create_post.html',form=form)    



