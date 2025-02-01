from flask import Blueprint
# from .routes import index  # Commented out because the module does not exist
from .routes import main


# Define un nombre único para este Blueprint
bp = Blueprint("index", __name__)  # Cambia "main" por un nombre único si tienes otros Blueprints
main = Blueprint('main', __name__)
# Importa las rutas específicas

