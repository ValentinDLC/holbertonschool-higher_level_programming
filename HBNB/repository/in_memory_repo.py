from typing import Dict, List, Optional, Any
from models.base_model import BaseModel

class InMemoryRepo:
    _storage: Dict[str, Dict[str, BaseModel]] = {
        'User ': {}, 'Place': {}, 'Review': {}, 'Amenity': {}
    }

    def get_all(self, model_class: str) -> List[BaseModel]:
        return list(self._storage.get(model_class, {}).values())

    def get(self, model_class: str, id: str) -> Optional[BaseModel]:
        return self._storage.get(model_class, {}).get(id)

    def create(self, obj: BaseModel):
        model_name = type(obj).__name__
        self._storage[model_name][obj.id] = obj
        return obj

    def update(self, model_class: str, id: str, **kwargs):
        obj = self.get(model_class, id)
        if obj:
            for key, value in kwargs.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
            obj.save()
            return obj
        return None

    def delete(self, model_class: str, id: str) -> bool:
        if id in self._storage.get(model_class, {}):
            del self._storage[model_class][id]
            return True
        return False
