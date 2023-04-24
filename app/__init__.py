from flask import Flask, g, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from .models import connect_db, db, User
from .utils import do_login, do_logout

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///memeo-demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SECRET_KEY'] = 'memeo-key'
    
    connect_db(app)
    db.init_app(app)
    
    migrate = Migrate(app, db)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .game import game_bp
    app.register_blueprint(game_bp)

    from .api import api_bp
    app.register_blueprint(api_bp)

    return app

app = create_app()

debug = DebugToolbarExtension(app)



