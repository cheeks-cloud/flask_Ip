from flask import render_template,request,redirect,url_for, abort
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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

