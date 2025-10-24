import uuid
from datetime import datetime
from typing import Optional, Dict, Any

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        created_at = kwargs.get('created_at')
        self.created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S') if created_at else datetime.now()
        updated_at = kwargs.get('updated_at', self.created_at)
        self.updated_at = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S') if updated_at else self.created_at

    def to_dict(self) -> Dict[str, Any]:
        d = {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            **{k: v for k, v in self.__dict__.items() if k not in ['created_at', 'updated_at', 'id', 'password'] if not k.startswith('_')}
        }
        # Exclure password pour tous, mais spécifique à User
        if hasattr(self, 'password'):
            d.pop('password', None)
        return d

    def save(self):
        self.updated_at = datetime.now()