from .extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')  # Ejemplo de roles: 'admin', 'user'

    def is_admin(self):
        return self.role == 'admin'

class DORReport(db.Model):
    __tablename__ = 'dor_reports'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    processed_data = db.Column(db.Text, nullable=True)

class TemplateFile(db.Model):
    __tablename__ = 'template_files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

def create_tables():
    """Crea las tablas en la base de datos."""
    db.create_all()