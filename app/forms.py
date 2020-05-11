from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired

class PostForm(FlaskForm):    
    title = TextAreaField('Title:', validators=[DataRequired()])
    body = TextAreaField('Body:', validators=[DataRequired()])
    submit = SubmitField('Submit')
