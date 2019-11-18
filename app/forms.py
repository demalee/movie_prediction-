from flask_wtf import FlaskForm
from wtforms import (StringField,
                     PasswordField,
                     SubmitField)
from  wtforms.validators import (DataRequired,
                                 Email)

class UserForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email Address", validators = [DataRequired(),
                                                       Email("Please enter a valid email  address")])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("submit")


class LoginForm(FlaskForm):
    email = StringField("Username", validators = [DataRequired(),Email("Please enter a valid email  address")])
    password = PasswordField("Password", validators = [DataRequired()])
    submit = SubmitField("login")


# movie forms
class MovieForm(FlaskForm):
    title = StringField("Movie / Series Title", validators =[DataRequired()])
    submit = SubmitField("Search")


