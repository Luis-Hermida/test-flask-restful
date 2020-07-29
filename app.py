from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

print("Starting Server...")

app = Flask(__name__)
app.secret_key = "key-1234567890"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)  # Allow us to add resources to app

# To change the authentication URL (Default: /auth)
app.config["JWT_AUTH_URL_RULE"] = "/auth"
# Config JWT to expire within half an hour (Default: 300)
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=1800)
# config JWT auth key name to be 'username' (Default: username)
app.config["JWT_AUTH_USERNAME_KEY"] = "username"


jwt = JWT(app, authenticate, identity)  # /auth

# Tell API that resource is now accesible in out API.
# http://127.0.0.1:5000/student/<name>
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
