from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)

from article.api import *
from article.views import *

if __name__ == "__main__":
    application.debug = True
    application.run(host='0.0.0.0')
