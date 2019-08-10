from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    '''
    Class to create a form for creating a blog
    '''
    title=StringField('Blog Title',validators=[DataRequired()])
    content=TextAreaField('Blog Content',validators=[DataRequired()])
    submit=SubmitField('Submit Post')
