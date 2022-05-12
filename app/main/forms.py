from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    category = TextAreaField('Post category', validators=[InputRequired()])
    about = TextAreaField('Post about', validators=[InputRequired()])
    votes=TextAreaField('Post votes', validators=[InputRequired()])
    submit = SubmitField('Submit')



class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[InputRequired()])
    Comment = TextAreaField('Comment review', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')



