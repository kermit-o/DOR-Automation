from flask import Flask
from .extensions import db, login
from .routes.routes import main
from .auth.routes import auth
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Inicializar extensiones
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    # Configurar el user_loader
    @login.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    login.login_view = "auth.login"  # Redirige a login si el usuario no está autenticado
    login.login_message = "Debes iniciar sesión para acceder a esta página."  # Mensaje de error

    # Registrar Blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    # Crear tablas dentro del contexto de la aplicación
    with app.app_context():
        db.create_all()

    return app