from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '').strip()

        # Validations
        if not self.name:
            raise ValueError('Name is required')
        if len(self.name) > 50:
            raise ValueError('Name must be less than 50 characters')
        # Uniqueness check should be handled in facade (e.g., check existing amenities)