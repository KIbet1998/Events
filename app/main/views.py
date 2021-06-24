
from flask import render_template,url_for,flash,redirect,request
from . import main
from flask_login import login_user,logout_user,login_required,current_user
from flask_sqlalchemy import SQLAlchemy
from .forms import PostForm
from ..models import Post, User
from .. import db
@main.route('/')
def index():
  posts=Post.query.all()
  heading = 'Working.. Good to go'
  return render_template('index.html', heading=heading,posts=posts)


@main.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form =PostForm()
    if form.validate_on_submit():
        
        title=form.title.data
        content=form.content.data
        user_id=current_user
        post=Post(title=title,content=content,user_id=current_user._get_current_object().id)

        db.session.add(post)
        db.session.commit()
        flash("Your post has been created",'success')
        return redirect(url_for('.index'))
    return render_template('create_post.html',form=form)

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
