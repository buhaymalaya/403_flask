from flask import Flask
from flask_smorest import Api
from flask_cors import CORS 
# after installations pip etc
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.user_model import UserModel

from resources.post import bp as post_bp
app.register_blueprint(post_bp)
from resources.user import bp as user_bp
app.register_blueprint(user_bp)

