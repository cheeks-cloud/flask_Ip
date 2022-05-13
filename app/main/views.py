from flask import render_template,request,redirect,url_for, abort
from .import main
from ..models import Comment, User,Post
from .forms import CommentForm,UpdateProfile,PitchForm
from flask_login import login_required,current_user
from .. import db,photos


@main.route('/')
def index():
    posts = Post.query.all()
    print(posts)
    
    return render_template('index.html',posts=posts)


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

        return redirect(url_for('main.update_profile',uname=user.username))

    return render_template('profile/update.html',form =form)
  

@main.route('/post',methods=['GET','POST'])
@login_required
def write_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        post = Post(category =form.category.data,about = form.about.data,votes=form.votes.data,writer = current_user.id)
    
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('auth.profile',uname=current_user.username))


    return render_template('posts.html',form = form)
    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        return redirect(url_for('auth.profile',uname=uname)) 



@main.route('/comment/<comment_id>/add/comment', methods = ['GET','POST'])
@login_required
def newComment(comment_id):
    print(comment_id)
    form = CommentForm() 
    if form.validate_on_submit():
        about = form.about.data 
        new_comment = Comment(about=about,writer=current_user.id,post=comment_id)
        db.session.add(new_comment)
        db.session.commit()
       
        return redirect(url_for('main.index'))
  
    return render_template('auth/comments.html',comment_form=form)


