from flask import render_template,request,redirect,url_for, abort
from .import main
from ..models import Comment, User
from .forms import CommentForm,UpdateProfile
from flask_login import login_required
from .. import db,photos




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


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname)) 