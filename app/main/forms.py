
from wtforms import StringField,SubmitField,TextAreaField,validators
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Post
from wtforms import ValidationError
from flask_wtf import FlaskForm


class PostForm(FlaskForm):
    title=StringField('Title',validators=[Required()])
    content=TextAreaField('Content',validators=[Required()])
    submit= SubmitField('Post')