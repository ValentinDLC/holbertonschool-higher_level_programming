from flask_restx import Api, Resource, fields
from flask import Blueprint

api_bp = Blueprint('api', __name__)
authorizations = {'apikey': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}}
api = Api(blueprint=api_bp, title='HBnB API', description='API RESTful pour HBnB (Partie 2)', authorizations=authorizations, security='apikey')

# Modèles pour serialization (Swagger)
user_model = api.model('User ', {
    'id': fields.String,
    'email': fields.String,
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'password': fields.String(required=True)  # Masqué en sortie via Facade
})

amenity_model = api.model('Amenity', {
    'id': fields.String,
    'name': fields.String(required=True)
})

place_model = api.model('Place', {
    'id': fields.String,
    'city_id': fields.String,
    'user_id': fields.String(required=True),
    'name': fields.String(required=True),
    'description': fields.String,
    'number_rooms': fields.Integer(default=0),
    'number_bathrooms': fields.Integer(default=0),
    'max_guest': fields.Integer(default=0),
    'price_by_night': fields.Float(required=True),
    'latitude': fields.Float,
    'longitude': fields.Float,
    'owner': fields.Nested(api.model('Owner', {
        'first_name': fields.String,
        'last_name': fields.String
    })),
    'amenities': fields.List(fields.Nested(amenity_model)),
    'reviews': fields.List(fields.Nested(api.model('ReviewSummary', {
        'id': fields.String,
        'text': fields.String
    })))
})

review_model = api.model('Review', {
    'id': fields.String,
    'place_id': fields.String(required=True),
    'user_id': fields.String(required=True),
    'text': fields.String(required=True),
    'place': fields.Nested(api.model('PlaceSummary', {'id': fields.String, 'name': fields.String})),
    'user': fields.Nested(api.model('User Summary', {'id': fields.String, 'first_name': fields.String, 'last_name': fields.String}))
})