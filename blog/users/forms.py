import wtforms as forms
from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from blog.models import User


class RegistrationForm(FlaskForm):
    username = forms.StringField("Username", validators=[DataRequired(), Length(min=5)])
    email = forms.EmailField("Email", validators=[DataRequired()])
    password = forms.PasswordField("Password", validators=[DataRequired()])
    confirm_password = forms.PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = forms.SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "That username is taken. Please choose a different one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")


class LoginForm(FlaskForm):
    email = forms.EmailField("Email", validators=[DataRequired()])
    password = forms.PasswordField("Password", validators=[DataRequired()])
    remember = forms.BooleanField("Remember Me")
    submit = forms.SubmitField("Login")


class ProfileForm(FlaskForm):
    username = forms.StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = forms.EmailField("Email", validators=[DataRequired()])
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = forms.SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "That username is taken. Please choose a different one."
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "That email is taken. Please choose a different one."
                )


class RequestResetForm(FlaskForm):
    email = forms.EmailField("Email", validators=[DataRequired()])
    submit = forms.SubmitField("Request Password Reset")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. You must register first."
            )


class ResetPasswordForm(FlaskForm):
    password = forms.PasswordField("Password", validators=[DataRequired()])
    confirm_password = forms.PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = forms.SubmitField("Reset Password")
