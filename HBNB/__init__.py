from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version="1.0", title="HBnB API", description="HBnB clone API")

# Import du facade
from HBNB.facade.facade import UserFacade
app.facade = UserFacade()

# Import des namespaces
from api.v1.users import users_ns
api.add_namespace(users_ns, path="/api/v1/users")
