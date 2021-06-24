from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class PostForm:
    title=StringField('Title',validators=[Required()])
    content=TextAreaField('Content',validators=[Required()])
    title= SubmitField('Post')