from flask import Blueprint, redirect, render_template, request, flash
from flask_app.models.user import User
from flask_app.extensions import bcrypt, db, login_manager
from flask_app.forms.register import RegisterForm
from flask_app.forms.login import LoginForm
from flask_login import login_required, login_user, logout_user

bp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    '''User loader for Flask-Login'''

    return User.query.get(int(user_id))

@bp.route("/auth/register", methods=["GET", "POST"])
def register():
    '''Displays the register form'''

    form = RegisterForm()

    if form.validate_on_submit():
        # Get Valid user input
        businessname = request.form.get("businessname")
        address = request.form.get("address")
        phone = request.form.get("phone")
        business_license = request.form.get("business_license")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if potential_user:
            flash("Email in use. Please log in", "warning")
            return redirect("/auth/login")
        # Hash the password
        hashed = bcrypt.generate_password_hash(password)
        # Create user, add to db
        new_user = User(
            businessname=businessname,
            address=address,
            phone=phone,
            business_license=business_license,
            email=email,
            password=hashed,
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in")
        return redirect("/auth/login")

    return render_template("/auth/register.html", form=form)


@bp.route("/auth/login", methods=["GET", "POST"])
def login():
    '''Display the home page with Log in form'''

    form = LoginForm()

    if form.validate_on_submit():
        # get the valid user input
        email = request.form.get("email")
        password = request.form.get("password")
        # Check if user's email exists
        potential_user = User.query.filter_by(email=email).first()
        if not potential_user:
            flash("Invalid credentials")
            return redirect ("/")
        
        user = potential_user

        #  Check password validity
        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid credentials")
            return redirect ("/")

        # Log the user in 
        login_user(user)
        return redirect("/dashboard")

    return render_template("/auth/login.html", form=form)


@bp.get("/auth/logout")
def logout():
    """Logs out the current user."""

    logout_user()
    return redirect("/")