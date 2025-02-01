from flask import Blueprint, request, render_template
from DORProject.app.models_backup import DORReport
from app import db
import os


template_bp = Blueprint('template_bp', __name__, template_folder='../templates')

@template_bp.route('/upload-template', methods=['POST'])
def upload_template():
    # Manejar la subida de la plantilla inicial
    pass


@template_bp.route('/template')
def template_route():
    return render_template('template.html')

