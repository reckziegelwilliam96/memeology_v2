from flask import session
from .models import User

def do_login(user_id):
    """Log in user."""

    session["user_id"] = user_id

def do_logout():
    """Log out user."""

    if "user_id" in session:
        del session["user_id"]