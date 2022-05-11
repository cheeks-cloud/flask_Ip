from flask import render_template,redirect,url_for, abort
from .import main
from ..models import Comment, User
from .forms import CommentForm
from flask_login import login_required




@main.route('/')
def index():

  return render_template('index.html')




@main.route('/', methods = ['GET','POST'])
@login_required
def new_comment(id):

    form = CommentForm()

    
    if form.validate_on_submit():
        post = form.post.data
       
        new_comment = Comment(post)
        new_comment.save_comment()

        return redirect(url_for())
  
    return render_template('comments.html',comment_form=form)



