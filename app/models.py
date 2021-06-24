from . import db
from . import login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    posts_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    liked = db.relationship('PostLike',foreign_keys='PostLike.user_id', backref='user', lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    def __repr__(self):
        return f"User('{self.username}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


    