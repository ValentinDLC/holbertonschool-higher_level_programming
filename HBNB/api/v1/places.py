from flask_restx import Namespace, Resource, reqparse
from app import api, app
from api.v1.restx import place_model

places_ns = Namespace('places', description='Opérations sur les places')

place_parser = reqparse.RequestParser()
place_parser.add_argument('city_id', type=str)
place_parser.add_argument('user_id', type=str, required=True, help='ID du propriétaire requis')
place_parser.add_argument('name', type=str, required=True, help='Nom requis')
place_parser.add_argument('description', type=str)
place_parser.add_argument('number_rooms', type=int, default=0)
place_parser.add_argument('number_bathrooms', type=int, default=0)
place_parser.add_argument('max_guest', type=int, default=0)
place_parser.add_argument('price_by_night', type=float, required=True, help='Prix par nuit requis (>0)')
place_parser.add_argument('latitude', type=float)
place_parser.add_argument('longitude', type=float)

update_parser = reqparse.RequestParser()
update_parser.add_argument('name', type=str)
update_parser.add_argument('description', type=str)
update_parser.add_argument('number_rooms', type=int)
update_parser.add_argument('number_bathrooms', type=int)
update_parser.add_argument('max_guest', type=int)
update_parser.add_argument('price_by_night', type=float)
update_parser.add_argument('latitude', type=float)
update_parser.add_argument('longitude', type=float)

@places_ns.route('')
class PlacesList(Resource):
    def get(self):
        """Récupérer la liste de toutes les places"""
        places = app.facade.get_places()
        return {'places': places}, 200

    @api.expect(place_model, validate=True)
    def post(self):
        """Créer une nouvelle place"""
        args = place_parser.parse_args()
        try:
            place = app.facade.create_place(**{k: v for k, v in args.items() if v is not None})
            return place, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@places_ns.route('/<string:place_id>')
@api.response(404, 'Place non trouvée')
class Place(Resource):
    def get(self, place_id):
        """Récupérer une place par ID (avec owner, amenities, reviews)"""
        place = app.facade.get_place(place_id)
        if place:
            return place, 200
        return {'error': 'Place non trouvée'}, 404

    @api.expect(update_parser, validate=True)
    def put(self, place_id):
        """Mettre à jour une place"""
        args = update_parser.parse_args()
        if not any([args[k] for k in args if args[k] is not None]):
            return {'error': 'Au moins un champ doit être fourni pour la mise à jour'}, 400
        try:
            updated = app.facade.update_place(place_id, **{k: v for k, v in args.items() if v is not None})
            if updated:
                return updated, 200
            return {'error': 'Place non trouvée'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400

@places_ns.route('/<string:place_id>/amenities/<string:amenity_id>')
class PlaceAmenity(Resource):
    def post(self, place_id, amenity_id):
        """Lier un amenity à une place"""
        if app.facade.link_amenity_to_place(place_id, amenity_id):
            return {'message': 'Amenity lié avec succès'}, 201
        return {'error': 'Place ou Amenity non trouvé'}, 404