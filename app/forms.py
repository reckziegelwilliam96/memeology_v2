from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, TextAreaField
from wtforms.fields.html5 import TelField
from wtforms.validators import InputRequired, Email, Length, Optional

class SignUpForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": "Enter your username. Make it fun and memeable!"})
    password = PasswordField('Password', validators=[Length(min=6)], render_kw={"placeholder": "Enter your password. Shh!"})
    email = StringField('E-mail', validators=[InputRequired(), Email()], render_kw={"placeholder": "Enter your email. (We promise not to email you)."})
    phone_number = TelField('Phone Number', validators=[Optional()], render_kw={"placeholder": "Enter your phone number. (We double promise not to text you)."})
    #avatar = RadioField('Avatar', choices=[('1', 'Avatar 1'), ('2', 'Avatar 2'), ('3', 'Avatar 3')])
    tagline = StringField('Tagline', validators=[Optional(), Length(max=50)], render_kw={"placeholder": "Enter an optional tagline, your call to arms. Is cute."})
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=100)], render_kw={"placeholder": "Enter an optional Bio. Could be cute?"})
    

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

