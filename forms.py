from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )

    class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = PasswordField("Email", validators=[InputRequired()])
    first_name = PasswordField("First Name", validators=[InputRequired()])
    last_name = PasswordField("Last Name", validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    text = StringField("Feedback", validators=[InputRequired()])
