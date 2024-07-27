# loyalty_service.py


 #from .models import User

 #def update_user_points(user_id,points_to_add=1):
   #  user = User.query.get(user_id)
     #if user:
       #  user.loyal_points + user.loyal_points  # Example: Increment points by 1
         #db.session.commit()
         #print(f"Loyalty points updated successfully for user ID {user_id}")
     #else:
       #  print(f"User with ID {user_id} not found")
#from flask import Flask, request, render_template, redirect, url_for # type: ignore
#import sqlite3
#from . import db

#app = Flask(__name__)

#def get_db_connection():
 #   conn = sqlite3.connect('new_db.sqlite')
  #  conn.row_factory = sqlite3.Row
   # return conn

#@app.route('/update_points', methods=['GET', 'POST'])
#def update_points():
 #   if request.method == 'POST':
  #      id = request.form['id']
   #     loyalty_points = request.form['loyalty_points']
        
    #    conn = get_db_connection()
     #   conn.execute('UPDATE users SET points = ? WHERE id = ?', (loyalty_points, id))
      #  conn.commit()
       # conn.close()
        
        #return redirect(url_for('update_points'))
    
    #return render_template('updloyal.html')
#if __name__ == '__main__':
  #  with app.app_context():
 #       db.create_all()
   # app.run(debug=True)
#from flask import current_app, request
#from flask_login import current_user, login_required
#from .models import User, db

#@main.route('/update_points', methods=['POST'])
#@login_required
#def update_points():
 #   loyalty_points = float(request.form.get('loyalty_points', 0.0))
    
    # Fetch the logged-in user's ID from Flask-Login's current_user object
    #user_id = current_user.id
    
    #user = User.query.get(user_id)
    
    #if user:
    #    if user.loyalty_points is None:
     #       user.loyalty_points = 0.0
      #  user.loyalty_points += loyalty_points
       # db.session.commit()
    
  #  return redirect(url_for('main.update_points'))



