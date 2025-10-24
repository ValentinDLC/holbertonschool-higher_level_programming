# Importe les classes principales (sans cycles)
from .base_model import BaseModel
from .user import User
from .amenity import Amenity
# Place et Review importés via Facade pour éviter cycles
