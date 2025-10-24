import unittest
import json
from app import app

class TestHbnbAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user_success(self):
        response = self.app.post('/api/v1/users/', json={
            'email': 'test@example.com',
            'password': 'secret123',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertNotIn('password', data)
        self.assertEqual(data['email'], 'test@example.com')

    def test_create_user_missing_email(self):
        response = self.app.post('/api/v1/users/', json={
            'password': 'secret123',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_create_user_invalid_email(self):
        response = self.app.post('/api/v1/users/', json={
            'email': 'invalid-email',
            'password': 'secret123',
            'first_name': 'John',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Format email invalide', data['error'])

    def test_get_users(self):
        response = self.app.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('users', data)

    def test_create_place_success(self):
        # Créez d'abord un user pour user_id
        user_resp = self.app.post('/api/v1/users/', json={
            'email': 'owner@example.com',
            'password': 'secret123',
            'first_name': 'Owner',
            'last_name': 'Test'
        })
        user_id = json.loads(user_resp.data)['id']
        response = self.app.post('/api/v1/places/', json={
            'user_id': user_id,
            'name': 'Test Place',
            'price_by_night': 100.0
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertIn('owner', data)

    def test_create_place_negative_price(self):
        response = self.app.post('/api/v1/places/', json={
            'user_id': 'dummy_id',  # Sera validé par Facade
            'name': 'Test Place',
            'price_by_night': -10.0
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Prix par nuit doit être positif', data['error'])

    def test_create_review_success(self):
        # Assume place et user créés ; pour test simple, ignore ID check (ajustez avec vrais IDs)
        response = self.app.post('/api/v1/reviews/', json={
            'place_id': 'dummy_place',
            'user_id': 'dummy_user',
            'text': 'Great stay!'
        })
        self.assertEqual(response.status_code, 201)  # Ou 400 si IDs invalides

    def test_create_review_empty_text(self):
        response = self.app.post('/api/v1/reviews/', json={
            'place_id': 'dummy',
            'user_id': 'dummy',
            'text': ''
        })
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('Texte de l\'avis requis et non vide', data['error'])

    def test_delete_review_nonexistent(self):
        response = self.app.delete('/api/v1/reviews/nonexistent')
        self.assertEqual(response.status_code, 404)

    # Ajoutez plus de tests pour amenities, update, etc.
    # Ex. : test_link_amenity_to_place

if __name__ == '__main__':
    unittest.main()