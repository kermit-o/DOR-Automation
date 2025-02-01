from flask import Blueprint, send_from_directory
import os

report_bp = Blueprint('report_bp', __name__)

@report_bp.route('/download/<filename>')
def download_report(filename):
    # Lógica para manejar la descarga de reportes
    pass

@report_bp.route('/reports', methods=['GET'])
def list_reports():
    # Mostrar los reportes generados
    pass
