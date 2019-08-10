from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email=StringField('Your Email Address',validators=[DataRequired(),Email()])
    username=StringField('Your name',validators=[DataRequired()])
    role=SelectField('Choose a role',choices=[('user','User'),('writer','Writer'),('text','Plain Text')])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match')])
    pass_confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Sign Up')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('That username is taken')    



class LoginForm(FlaskForm):
    email=StringField('Your Email Address',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Sign In')

    
