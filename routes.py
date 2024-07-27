#from flask import Blueprint, request, jsonify # type: ignore
#from .loyal import update_user_points # type: ignore
#from .models import db, User

#update_loyalty_points = Blueprint('update_loyalty_points', __name__)

#@update_loyalty_points.route('/api/updateLoyaltyPoints', methods=['POST'])
#def update_loyalty_points_handler():
 #   data = request.get_json()
  #  user_id = data.get('user_id')
    # loyalty_points = data.get('loyalty_points')

     #if user_id is None:

       #  return jsonify({'error': 'Missing user_id or loyalty_points parameter'}), 400

     #user = User.query.get(user_id)
     #if user:
       #  user.loyalty_points += loyalty_points
         #db.session.commit()
         #return jsonify({'message': f'Loyalty points updated successfully for user ID {user_id}'}), 200
     #else:
       #  return jsonify({'error': f'User with ID {user_id} not found'}), 404
