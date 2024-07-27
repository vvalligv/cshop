import json
import logging

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session, current_app # type: ignore
from flask_login import current_user, login_user, login_required # type: ignore
from flask import make_response # type: ignore
from .models import User  # Assuming you have a User model defined
from . import db
from werkzeug.security import check_password_hash # type: ignore

main = Blueprint("main", __name__)

@main.route('/')
def index():
    return render_template("index.html")
    
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(Email=email).first()
        
        if user and check_password_hash(user.Password, password):
            login_user(user)
            resp = make_response(redirect(url_for('main.index')))
            resp.set_cookie('loyalty_points', str(user.loyalty_points))
            return resp
        else:
            flash('Invalid email or password.')
            return redirect(url_for('main.login'))
    
    return render_template('login.html')

@main.route('/registration')
def registration():
    return render_template("registration.html")

@main.route('/menu')
def menu():
    return render_template("menu.html")

@main.route('/entry')
def entry():
    return render_template("entry.html")

@main.route('/review')
def review():
    product = request.args.get('product')
    quantity = request.args.get('quantity')
    if not product or not quantity:
        return "Product or quantity missing", 400  # Return a 400 Bad Request if data is missing
    return render_template("review_cart.html", product=product, quantity=quantity)

@main.route('/cookiesindex')
def cookiesindex():
    return render_template("cookiesindex.html")

@main.route('/api/getUserId', methods=['GET'])
def get_user_id():
    if current_user.is_authenticated:
        return jsonify({'userId': current_user.id}), 200
    else:
        return jsonify({'error': 'User not authenticated'}), 401

@main.route('/pay')
def pay():
    return render_template("pay.html") 

@main.route('/confirm')
def confirm():
    return render_template("confirm.html")  

@main.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        # Here you would typically send an email to reset the password
        # For simplicity, we just redirect to login
        return render_template("login.html", message="")
    return render_template("forgot_password.html")

@main.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would typically send an email to the site admin or store the message in a database
        # For simplicity, let's assume printing the message to the console
        print(f"New Message:\nName: {name}\nEmail: {email}\nMessage: {message}")

        # Redirect to a thank you page or display a message
        return redirect(url_for('main.thankyou'))
    return render_template('index.html')

@main.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@main.route('/update_points', methods=['GET', 'POST'])
@login_required
def update_points():
    if request.method == 'POST':
        try:
            user_id = request.form.get('user_id')
            loyalty_points = request.form.get('loyalty_points')

            if not user_id or not loyalty_points:
                flash('User ID and loyalty points are required.')
                return redirect(url_for('main.update_points'))

            try:
                loyalty_points = float(loyalty_points)
            except ValueError:
                flash('Invalid loyalty points value.')
                return redirect(url_for('main.update_points'))

            user = User.query.get(user_id)
            if user:
                user.loyalty_points += loyalty_points
                db.session.commit()

                resp = make_response(redirect(url_for('main.update_points')))
                resp.set_cookie('loyalty_points', str(user.loyalty_points))
                return resp
            else:
                flash(f"User with ID {user_id} not found.")
                return redirect(url_for('main.update_points'))
        except Exception as e:
            current_app.logger.error(f'An error occurred while updating points: {e}')
            flash('An error occurred while updating points.')
            return redirect(url_for('main.update_points'))
    return render_template('update_points.html')




# Configure logging
logging.basicConfig(level=logging.DEBUG)

@main.route('/updateLoyaltyPoints', methods=['POST'])
def update_loyalty_points():
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'message': 'No data provided'}), 400
    
    email = data.get('email')
    loyalty_points = data.get('loyalty_points')
    
    if not email or not isinstance(loyalty_points, (int, float)):
        return jsonify({'success': False, 'message': 'Invalid data'}), 400

    user = User.query.filter(func.lower(User.Email) == func.lower(email)).first() # type: ignore
    
    if user:
        try:
            user.loyalty_points += loyalty_points
            db.session.commit()
            return jsonify({'success': True}), 200
        except Exception as e:
            current_app.logger.error(f'Error updating loyalty points: {e}')
            return jsonify({'success': False, 'message': 'Database error'}), 500
    else:
        return jsonify({'success': False, 'message': 'User not found'}), 404


@main.route('/api/checkEmail', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'exists': False}), 400

    user = User.query.filter(func.lower(User.email) == func.lower(email)).first() # type: ignore

    return jsonify({'exists': bool(user)})
    # Check if email exists in the database
   
  