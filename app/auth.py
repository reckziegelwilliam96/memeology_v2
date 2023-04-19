from flask import Blueprint, render_template, request, flash, redirect, session, g, current_app
from sqlalchemy.exc import IntegrityError
from .forms import SignUpForm, LoginForm
from .models import User, db
from .utils import do_login, do_logout

auth_bp = Blueprint('auth', __name__)

@auth_bp.before_app_request
def add_user_to_g():
    """If user is logged in, add the user object to Flask global."""
    if "user_id" in session:
        g.user = User.query.get(session["user_id"])
    else:
        g.user = None


@auth_bp.route('/signup', methods=["GET", "POST"])
def sign_up():
    """Handle user signup."""

    form = SignUpForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                phone_number=form.phone_number.data if form.phone_number.data else "N/A",
                tagline=form.tagline.data if form.tagline.data else "Yet to have my own catchphrase!",
                bio=form.bio.data if form.bio.data else "I don't have any hobbies. Memeo is my life."
            )
            db.session.commit()

        except IntegrityError:
            flash('Username taken', 'danger')
            return render_template('/users/signup.html', form=form)
        
        do_login(user.id)

        return redirect('/')
    
    else:
        return render_template('/users/signup.html', form=form)

@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                form.password.data)
        
        if user:
            do_login(user, current_app.config['CURR_USER_KEY'])
            flash(f"Welcome back, {user.username}", 'success')

            return redirect('/')

        flash("Invalid credentials", 'danger')

    return render_template('/users/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    """Handle user logout."""
    user = g.user

    if user:
        do_logout(current_app.config['CURR_USER_KEY'])
        flash(f"Until next time, {user.username}!", 'success')

        return redirect('/')

    form = UserAddForm()
    return render_template("users/signup.html", form=form)
