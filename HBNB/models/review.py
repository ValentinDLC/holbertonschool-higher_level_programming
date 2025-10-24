from __future__ import annotations  # Pour forward refs

from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', '')
        self.user_id = kwargs.get('user_id', '')
        self.text = kwargs.get('text', '').strip()

        # Validations
        if not self.place_id:
            raise ValueError('ID de la place requis')
        if not self.user_id:
            raise ValueError('ID de l\'user requis')
        if not self.text:
            raise ValueError('Texte de l\'avis requis et non vide')
        if len(self.text) > 1024:
            raise ValueError('Texte trop long (max 1024 caractères)')

    @property
    def place(self):
        from repository.in_memory_repo import InMemoryRepo
        from models.place import Place  # Import local (lazy)
        repo = InMemoryRepo()
        return repo.get('Place', self.place_id)

    @property
    def user(self):
        from repository.in_memory_repo import InMemoryRepo
        from models.user import User  # Import local (lazy)
        repo = InMemoryRepo()
        return repo.get('User ', self.user_id)
