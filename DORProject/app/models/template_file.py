# Archivo: models/template_file.py
# Define el modelo TemplateFile.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TemplateFile(db.Model):
    __tablename__ = 'template_files'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())