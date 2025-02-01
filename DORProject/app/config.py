import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(BASE_DIR, 'instance')
    os.makedirs(instance_path, exist_ok=True)  # Crear el directorio si no existe
    db_path = os.path.join(instance_path, 'dor_reports.db')
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "default_secret_key"