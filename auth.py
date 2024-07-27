from curses import window
from flask import Blueprint, render_template, request, url_for, redirect, flash # type: ignore
from .models import User
from flask_login import login_user, logout_user, login_required # type: ignore
from . import db
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore

auth = Blueprint("auth", __name__)

@auth.route('/registration', methods=['POST'])
def registration():
    FullName = request.form.get('FullName')
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    Confirm_Password = request.form.get('Confirm_Password')

    # Check if passwords match
    if Password != Confirm_Password:
        flash('Passwords do not match', 'error')
        return redirect(url_for('auth.registration'))

    # Check if the email already exists in the database
    user = User.query.filter_by(Email=Email).first()
    if user:
        flash('Email address already exists', 'error')
        return redirect(url_for('auth.registration'))

    try:
        # Create a new user with the form data
        new_user = User(
            FullName=FullName,
            Email=Email,
            Password=generate_password_hash(Password, method='pbkdf2:sha256')
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Debug statement
        print(f"User {Email} created successfully")

        # Redirect to the login page
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))
    except Exception as e:
        # Debug statement
        print(f"Error creating user: {e}")
        flash('An error occurred while creating the account. Please try again.', 'error')
        db.session.rollback()
        return redirect(url_for('auth.registration'))

@auth.route('/login', methods=['POST'])
def login_post():
    Email = request.form.get('Email')
    Password = request.form.get('Password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(Email=Email).first()
    if not user or not check_password_hash(user.Password, Password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # Redirect to the login page on login failure

    login_user(user, remember=remember)
    return redirect(url_for('main.menu'))


@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
