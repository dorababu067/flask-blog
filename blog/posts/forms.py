import wtforms as forms
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = forms.StringField("Title", validators=[DataRequired()])
    content = forms.TextAreaField("Content", validators=[DataRequired()])
    submit = forms.SubmitField("Post")
