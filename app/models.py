from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique=True,index=True)
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  pass_secure = db.Column(db.String(255))
  post = db.relationship('Post',backref = 'users',lazy="dynamic")
  comment = db.relationship('Comment',backref = 'users',lazy="dynamic")
 
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


      

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80),nullable=False)
    about= db.Column(db.Text,nullable=False)
    writer = db.Column(db.Integer,db.ForeignKey('users.id'))
    votes = db.Column(db.Integer,nullable=False)
    comment = db.relationship('Comment', backref='posts',lazy='dynamic')

    def get_posts():
        posts = Post.query.all()
        return posts
    def get_writer(self,id):
        writer =User.query.filter_by(id).first()
        return writer.username

    def get_comments(self,post):
        all_comments = Comment.query.filter_by(post).all()
        return all_comments

 

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer,primary_key=True)
    about=db.Column(db.Text,nullable=False)
    post=db.Column(db.Integer,db.ForeignKey('posts.id'))
    writer = db.Column(db.Integer,db.ForeignKey('users.id'))
   
   
    def get_writer(self):
        writer = User.query.filter_by(id=self.id).first()
        return writer

    def get_post(self):
        post = Post.query.filter_by(id=self.id).first()
        return post
   
   
   
   
   
   
   
   
   
