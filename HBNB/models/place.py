from __future__ import annotations  # Pour forward refs simples

from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from typing import List

class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.city_id = kwargs.get('city_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.name = kwargs.get('name', '').strip()
        self.description = kwargs.get('description', '').strip()
        self.number_rooms = int(kwargs.get('number_rooms', 0))
        self.number_bathrooms = int(kwargs.get('number_bathrooms', 0))
        self.max_guest = int(kwargs.get('max_guest', 0))
        self.price_by_night = float(kwargs.get('price_by_night', 0))
        lat = kwargs.get('latitude')
        self.latitude = float(lat) if lat is not None else None
        lon = kwargs.get('longitude')
        self.longitude = float(lon) if lon is not None else None
        self.amenities: List[Amenity] = []
        self.reviews: List['Review'] = []  # Forward ref (string)

        # Validations
        if not self.user_id:
            raise ValueError('ID du propriétaire (user_id) requis')
        if not self.name:
            raise ValueError('Nom de la place requis')
        if self.price_by_night <= 0:
            raise ValueError('Prix par nuit doit être positif')
        if self.number_rooms < 0 or self.number_bathrooms < 0 or self.max_guest < 0:
            raise ValueError('Nombre de chambres/salles de bain/invités doit être >= 0')
        if self.latitude is not None and (self.latitude < -90 or self.latitude > 90):
            raise ValueError('Latitude doit être entre -90 et 90')
        if self.longitude is not None and (self.longitude < -180 or self.longitude > 180):
            raise ValueError('Longitude doit être entre -180 et 180')
        if self.description and not self.description:
            raise ValueError('Description ne peut pas être vide si fournie')

    def add_amenity(self, amenity: Amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.save()

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)
            self.save()

    @property
    def owner(self):
        from repository.in_memory_repo import InMemoryRepo
        repo = InMemoryRepo()
        return repo.get('User ', self.user_id)

    @property
    def amenities_list(self):
        return self.amenities

    @property
    def reviews_list(self):
        from repository.in_memory_repo import InMemoryRepo
        from models.review import Review  # Import local (lazy)
        repo = InMemoryRepo()
        return [repo.get('Review', r.id) for r in self.reviews if r and hasattr(r, 'id')]
