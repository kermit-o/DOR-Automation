from flask import Blueprint, request
from DORProject.app.models_backup import DORReport
from app import db
import pandas as pd
import os

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload-additional', methods=['POST'])
def upload_additional_file():
    # Manejar la subida de archivos adicionales
    pass
