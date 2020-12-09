from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os
import connexion


basedir = os.path.abspath(os.path.dirname(__file__))


connex_app = connexion.App(__name__, specification_dir=basedir)


app = connex_app.app


app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "schedule.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


ma = Marshmallow(app)
