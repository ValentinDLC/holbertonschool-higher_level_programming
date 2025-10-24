from typing import List, Optional, Dict, Any
from repository.in_memory_repo import InMemoryRepo
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class HbnbFacade:
    def __init__(self):
        self.repo = InMemoryRepo()

    # Users
    def create_user(self, **kwargs) -> Dict[str, Any]:
        # Vérif unicité email
        for user in self.repo.get_all('User '):
            if user.email == kwargs.get('email'):
                raise ValueError('Email déjà utilisé')
        user = User(**kwargs)
        self.repo.create(user)
        user_dict = user.to_dict()
        return user_dict  # Password déjà exclu dans to_dict

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        user = self.repo.get('User ', user_id)
        return user.to_dict() if user else None

    def get_users(self) -> List[Dict[str, Any]]:
        users = self.repo.get_all('User ')
        return [u.to_dict() for u in users]

    def update_user(self, user_id: str, **kwargs) -> Optional[Dict[str, Any]]:
        updated = self.repo.update('User ', user_id, **kwargs)
        return updated.to_dict() if updated else None

    # Amenities
    def create_amenity(self, **kwargs) -> Dict[str, Any]:
        name = kwargs.get('name')
        for amenity in self.repo.get_all('Amenity'):
            if amenity.name == name:
                raise ValueError('Équipement déjà existant')
        amenity = Amenity(**kwargs)
        self.repo.create(amenity)
        return amenity.to_dict()

    def get_amenity(self, amenity_id: str) -> Optional[Dict[str, Any]]:
        amenity = self.repo.get('Amenity', amenity_id)
        return amenity.to_dict() if amenity else None

    def get_amenities(self) -> List[Dict[str, Any]]:
        amenities = self.repo.get_all('Amenity')
        return [a.to_dict() for a in amenities]

    def update_amenity(self, amenity_id: str, **kwargs) -> Optional[Dict[str, Any]]:
        updated = self.repo.update('Amenity', amenity_id, **kwargs)
        return updated.to_dict() if updated else None

    # Places
    def create_place(self, **kwargs) -> Dict[str, Any]:
        user_id = kwargs.get('user_id')
        if not self.repo.get('User ', user_id):
            raise ValueError('Propriétaire (user_id) non trouvé')
        place = Place(**kwargs)
        self.repo.create(place)
        return self._serialize_place(place)

    def get_place(self, place_id: str) -> Optional[Dict[str, Any]]:
        place = self.repo.get('Place', place_id)
        return self._serialize_place(place) if place else None

    def get_places(self) -> List[Dict[str, Any]]:
        places = self.repo.get_all('Place')
        return [self._serialize_place(p) for p in places]

    def update_place(self, place_id: str, **kwargs) -> Optional[Dict[str, Any]]:
        self.repo.update('Place', place_id, **kwargs)
        return self.get_place(place_id)

    def link_amenity_to_place(self, place_id: str, amenity_id: str) -> bool:
        place = self.repo.get('Place', place_id)
        amenity = self.repo.get('Amenity', amenity_id)
        if place and amenity:
            place.add_amenity(amenity)
            return True
        return False

    def _serialize_place(self, place: Place) -> Dict[str, Any]:
        p_dict = place.to_dict()
        owner = place.owner
        if owner:
            p_dict['owner'] = {'first_name': owner.first_name, 'last_name': owner.last_name}
        p_dict['amenities'] = [a.to_dict() for a in place.amenities_list]
        p_dict['reviews'] = [r.to_dict() for r in place.reviews_list]
        return p_dict

    # Reviews
    def create_review(self, **kwargs) -> Dict[str, Any]:
        place_id = kwargs.get('place_id')
        user_id = kwargs.get('user_id')
        if not self.repo.get('Place', place_id):
            raise ValueError('Place non trouvée')
        if not self.repo.get('User ', user_id):
            raise ValueError('User  non trouvé')
        # Vérif unicité
        for review in self.get_reviews_by_place(place_id):
            if review.get('user_id') == user_id:
                raise ValueError('Review déjà existante pour cet user et cette place')
        review = Review(**kwargs)
        self.repo.create(review)
        # Lier à place
        place = self.repo.get('Place', place_id)
        if place:
            place.add_review(review)
        return review.to_dict()

    def get_review(self, review_id: str) -> Optional[Dict[str, Any]]:
        review = self.repo.get('Review', review_id)
        if review:
            r_dict = review.to_dict()
            place = review.place
            user = review.user
            r_dict['place'] = {'id': review.place_id, 'name': place.name if place else ''}
            r_dict['user'] = {'id': review.user_id, 'first_name': user.first_name if user else '', 'last_name': user.last_name if user else ''}
            return r_dict
        return None

    def get_reviews(self) -> List[Dict[str, Any]]:
        reviews = self.repo.get_all('Review')
        return [r.to_dict() for r in reviews]

    def update_review(self, review_id: str, **kwargs) -> Optional[Dict[str, Any]]:
        updated = self.repo.update('Review', review_id, **kwargs)
        return updated.to_dict() if updated else None

    def delete_review(self, review_id: str) -> bool:
        return self.repo.delete('Review', review_id)

    def get_reviews_by_place(self, place_id: str) -> List[Dict[str, Any]]:
        reviews = self.repo.get_all('Review')
        filtered = [r for r in reviews if r.place_id == place_id]
        return [r.to_dict() for r in filtered]