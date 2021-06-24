from flask import render_template
from . import main

@main.route('/')
def index():
  posts=Post.query.all()
  heading = 'Working.. Good to go'
  return render_template('index.html', heading=heading)

@main.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form =PostForm()
    if form.validate_on_submit():
        post =Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created",'success')
        return redirect(url_for('.home'))
    return render_template('create_post.html',form=form)