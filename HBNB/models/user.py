from .base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '').strip()
        self.password = kwargs.get('password', '').strip()
        self.first_name = kwargs.get('first_name', '').strip()
        self.last_name = kwargs.get('last_name', '').strip()

        # Validations
        if not self.email:
            raise ValueError('Email est requis')
        if '@' not in self.email or not re.match(r'^[^@]+@[^@]+\.[^@]+$', self.email):
            raise ValueError('Format email invalide')
        if not self.password or len(self.password) < 6:
            raise ValueError('Mot de passe doit faire au moins 6 caractères')
        if not self.first_name:
            raise ValueError('Prénom requis')
        if not self.last_name:
            raise ValueError('Nom requis')