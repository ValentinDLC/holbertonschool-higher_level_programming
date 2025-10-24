from flask_restx import Namespace, Resource, reqparse
from app import api, app
from api.v1.restx import review_model

reviews_ns = Namespace('reviews', description='Opérations sur les reviews')

review_parser = reqparse.RequestParser()
review_parser.add_argument('place_id', type=str, required=True, help='ID de la place requis')
review_parser.add_argument('user_id', type=str, required=True, help='ID de l\'user requis')
review_parser.add_argument('text', type=str, required=True, help='Texte de l\'avis requis')

update_parser = reqparse.RequestParser()
update_parser.add_argument('text', type=str, required=True)

@reviews_ns.route('')
class ReviewsList(Resource):
    def get(self):
        """Récupérer la liste de toutes les reviews"""
        reviews = app.facade.get_reviews()
        return {'reviews': reviews}, 200

    @api.expect(review_model, validate=True)
    def post(self):
        """Créer une nouvelle review"""
        args = review_parser.parse_args()
        try:
            review = app.facade.create_review(**args)
            return review, 201
        except ValueError as e:
            return {'error': str(e)}, 400

@reviews_ns.route('/<string:review_id>')
@api.response(404, 'Review non trouvée')
class Review(Resource):
    def get(self, review_id):
        """Récupérer une review par ID (avec place et user)"""
        review = app.facade.get_review(review_id)
        if review:
            return review, 200
        return {'error': 'Review non trouvée'}, 404

    @api.expect(update_parser, validate=True)
    def put(self, review_id):
        """Mettre à jour une review"""
        args = update_parser.parse_args()
        try:
            updated = app.facade.update_review(review_id, text=args['text'])
            if updated:
                return updated, 200
            return {'error': 'Review non trouvée'}, 404
        except ValueError as e:
            return {'error': str(e)}, 400

    def delete(self, review_id):
        """Supprimer une review"""
        if app.facade.delete_review(review_id):
            return None, 200
        return {'error': 'Review non trouvée'}, 404

@reviews_ns.route('/places/<string:place_id>')
@api.response(404, 'Place non trouvée')
class PlaceReviews(Resource):
    def get(self, place_id):
        """Récupérer toutes les reviews d'une place spécifique"""
        place = app.facade.get_place(place_id)
        if not place:
            return {'error': 'Place non trouvée'}, 404
        reviews = app.facade.get_reviews_by_place(place_id)
        return {'reviews': reviews}, 200