from flask import Flask
from flask_mail import Mail
from blog.config import Config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


mail = Mail()
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message_category = "info"


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # import Blueprints here.
    from blog.main.views import main
    from blog.posts.views import posts
    from blog.users.views import users

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)

    return app
