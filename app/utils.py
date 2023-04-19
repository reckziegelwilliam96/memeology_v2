from flask import session

def do_login(user, CURR_USER_KEY):
    """Log in user."""

    session[CURR_USER_KEY] = user.id

def do_logout(CURR_USER_KEY):
    """Log out user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]