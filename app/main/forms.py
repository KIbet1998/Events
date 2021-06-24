from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Post
from wtforms import ValidationError,validators



class PostForm:
    title=StringField('Title',validators=[Required()])
    content=TextAreaField('Content',validators=[Required()])
    title= SubmitField('Post')