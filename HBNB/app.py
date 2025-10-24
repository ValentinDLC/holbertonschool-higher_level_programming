from flask import Flask
from api.v1.restx import api
from facade.hbnb_facade import HbnbFacade

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
api.init_app(app)

facade = HbnbFacade()
app.facade = facade

# Ajout des namespaces
from api.v1.users import api as users_ns
from api.v1.amenities import api as amenities_ns
from api.v1.places import api as places_ns
from api.v1.reviews import api as reviews_ns

api.add_namespace(users_ns, path='/api/v1/')
api.add_namespace(amenities_ns, path='/api/v1/')
api.add_namespace(places_ns, path='/api/v1/')
api.add_namespace(reviews_ns, path='/api/v1/')

if __name__ == '__main__':
    app.run(debug=True)
