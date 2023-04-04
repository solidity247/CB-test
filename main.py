import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, firestore
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask import render_template 
import json
# test 
app = Flask(__name__)
CORS(app)

os.environ['GOOGLE_CLOUD_PROJECT'] = 'test-proj-382602'
firebase_admin.initialize_app()
db = firestore.client()

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     display_name = data.get('displayName')
    
#     try:
#         user = auth.create_user(
#             email=email,
#             password=password,
#             display_name=display_name
#         )
#         user_ref = db.collection('users').document(user.uid)
#         user_ref.set({
#             'email': email,
#             'displayName': display_name,
#             'photoURL': None,
#             'role': 'individual',
#             'organizationId': None,
#             'carbonFootprint': 0,
#             'achievements': [],
#             'goals': [],
#             'connections': []
#         })
#         return jsonify({'success': True, 'userId': user.uid}), 201
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 400

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
    
#     try:
#         user = auth.get_user_by_email(email)
#         if user and auth.verify_password(password, user.password_hash):
#             return jsonify({'success': True, 'userId': user.uid}), 200
#         else:
#             return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
#     except Exception as e:
#         return jsonify({'success': False, 'error': str(e)}), 400

 
@app.route('/carbon-footprint/<user_id>', methods=['GET'])
def get_carbon_footprint(user_id):
    try:
        user_ref = db.collection('users').document(user_id)
        user_data = user_ref.get().to_dict()
        if user_data:
            carbon_footprint =  user_data['carbonFootprint']
            return render_template('carbon_footprint.html', carbon_footprint=carbon_footprint)
        else:
            return jsonify({'success': False, 'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
