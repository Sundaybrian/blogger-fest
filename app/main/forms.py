from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email
from . import User


class PostForm(FlaskForm):
    '''
    Class to create a form for creating a blog
    '''
    title=StringField('Blog Title',validators=[DataRequired()])
    content=TextAreaField('Blog Content',validators=[DataRequired()])
    submit=SubmitField('Submit Post')

class CommentForm(FlaskForm):
    '''
    class to create a comment form
    '''
    comment_content=TextAreaField('Comment',validators=[DataRequired()])
    submit=SubmitField('Submit')

class UpdateProfile(FlaksForm):
    '''
    class to create a form to update user details
    '''
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    submit=SubmitField('Update')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('That username is taken')    




    
    

