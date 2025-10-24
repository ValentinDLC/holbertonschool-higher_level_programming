from flask_restx import Namespace, Resource, reqparse
from app import api, app
from api.v1.restx import amenity_model

amenities_ns = Namespace('amenities', description='Opérations sur les amenities')

amenity_parser = reqparse.RequestParser()
amenity_parser.add_argument('name', type=str, required=True, help='Nom de l\'équipement requis')

update_parser = reqparse.RequestParser()
update_parser.add_argument('name', type=str)

@amenities_ns.route('')
class AmenitiesList(Resource):
    def get(self):
        """Récupérer la liste de tous les amenities"""
        amenities = app.facade.get_amenities()
        return {'amenities': amenities}, 200

    @api.expect(amenity_model, validate=True)
    def post(self):
        """Créer un nouvel amenity"""
        args = amenity_parser.parse_args()
        try:
            amenity = app.facade.create_amenity(**args)
            return amenity, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@amenities_ns.route('/<string:amenity_id>')
@api.response(404, 'Amenity non trouvé')
class Amenity(Resource):
    def get(self, amenity_id):
        """Récupérer un amenity par ID"""
        amenity = app.facade.get_amenity(amenity_id)
        if amenity:
            return amenity, 200
        return {'error': 'Amenity non trouvé'}, 404

    @api.expect(update_parser, validate=True)
    def put(self, amenity_id):
        """Mettre à jour un amenity"""
        args = update_parser.parse_args()
        if not args['name']:
            return {'error': 'Nom requis pour la mise à jour'}, 400
        try:
            updated = app.facade.update_amenity(amenity_id, name=args['name'])
            if updated:
                return updated, 200
            return {'error': 'Amenity non trouvé'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400