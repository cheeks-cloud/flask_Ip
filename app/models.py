from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique=True,index=True)
  role_id =db.Column(db.Integer,db.ForeignKey('roles.id')) 
  pass_secure = db.Column(db.String(255)) @property

  
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



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}' 

class Comment:
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
