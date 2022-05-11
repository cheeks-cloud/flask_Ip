from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique=True,index=True)
#   comment = db.relationship('comment', backref='all_users',lazy='dynamic')
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pass_secure = db.Column(db.String(255))

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
    return f'User {self.username}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80),)
    on = db.Column(db.Text,)
    votes = db.Column(db.Integer,)
    comment = db.relationship('comment', backref='all_users',lazy='dynamic')

    def get_posts():
        pass
    def get_comments():
        pass

 

class Comment():
    all_comments = []

    def __init__(self,post):
        self.post = post

    def save_comment(self):
        Comment.all_comments.append(self)

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

#to display all comment for a particular post
    @classmethod
    def get_comments(cls,id):
        response = []

        for comment in cls.all_comments:
            if comment.post_id == id:
                response.append(comment)

        return response
