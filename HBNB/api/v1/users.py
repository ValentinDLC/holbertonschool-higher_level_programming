from flask_restx import Namespace, Resource, reqparse
from app import api, app
from api.v1.restx import user_model

users_ns = Namespace('users', description='User operations')

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, required=True, help='Email is required')
user_parser.add_argument('password', type=str, required=False)
user_parser.add_argument('first_name', type=str, required=True, help='First name is required')
user_parser.add_argument('last_name', type=str, required=True, help='Last name is required')

update_parser = reqparse.RequestParser()
update_parser.add_argument('email', type=str)
update_parser.add_argument('first_name', type=str)
update_parser.add_argument('last_name', type=str)

@users_ns.route('')
class UsersList(Resource):
    def get(self):
        """Get all users"""
        users = app.facade.get_users()
        return {'users': users}, 200

    @api.expect(user_model, validate=True)
    def post(self):
        """Create a new user"""
        args = user_parser.parse_args()
        try:
            user = app.facade.create_user(**args)
            return user, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@users_ns.route('/<string:user_id>')
@api.response(404, 'User not found')
class User(Resource):
    def get(self, user_id):
        """Get user by ID"""
        user = app.facade.get_user(user_id)
        if user:
            return user, 200
        return {'error': 'User not found'}, 404

    @api.expect(update_parser, validate=True)
    def put(self, user_id):
        """Update user"""
        args = update_parser.parse_args()
        if not any([args['email'], args['first_name'], args['last_name']]):
            return {'error': 'At least one field must be provided for update'}, 400
        try:
            updated = app.facade.update_user(user_id, **{k: v for k, v in args.items() if v is not None})
            if updated:
                return updated, 200
            return {'error': 'User not found'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400
