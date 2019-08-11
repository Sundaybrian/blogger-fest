from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField

#for the picture upload
from flask_wtf.file import FileField,FileAllowed

from wtforms import ValidationError
from wtforms.validators import DataRequired,Email
from ..models import User


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

class UpdateProfileForm(FlaskForm):
    '''
    class to create a form to update user details
    '''
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username',validators=[DataRequired()])
    pictures=FileField('Update Profile Pic',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')

    def validate_email(self,field):

        if User.query.filter_by(email=field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('That username is taken')    




    
    

