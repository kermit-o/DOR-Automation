# Archivo: models/dor_report.py
# Define el modelo DORReport.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DORReport(db.Model):
    __tablename__ = 'dor_reports'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    processed_data = db.Column(db.Text, nullable=True)