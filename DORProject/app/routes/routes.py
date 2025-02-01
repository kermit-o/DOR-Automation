from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory, flash, after_this_request
from flask_login import current_user, login_required
import os
from ..models import DORReport, User    
from ..utils.upload_handler import handle_file_upload
from ..utils.pdf_utils import export_report_to_pdf
from ..extensions import db, login, LoginManager

UPLOAD_FOLDER = 'uploads'
PUBLIC_FOLDER = '/var/www/html/download'
DOR_FILE = "DOR.xlsx"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PUBLIC_FOLDER, exist_ok=True)

main = Blueprint('main', __name__, template_folder='../templates')

@login.user_loader
@main.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))  # 🔴 Redirige al login si no está autenticado
    return render_template('dashboard.html', user=current_user)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/reports', methods=['GET', 'POST'])
@login_required
def list_reports():
    if request.method == 'POST':
        filter_filename = request.form.get('filename')
        if filter_filename:
            reports = DORReport.query.filter(DORReport.filename.contains(filter_filename)).all()
        else:
            reports = DORReport.query.all()
    else:
        reports = DORReport.query.all()

    return render_template('reports.html', reports=reports)

@login_required
@main.route('/download/<filename>')
def download_file(filename):
    @after_this_request
    def remove_file(response):
        try:
            os.remove(os.path.join(PUBLIC_FOLDER, filename))
            print(f"Removed file {filename} from public folder")
        except Exception as e:
            print(f"Error removing file {filename}: {e}")
        return response

    return send_from_directory(PUBLIC_FOLDER, filename)

@login_required
@main.route('/files')
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('files.html', files=files)

@login_required
@main.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        os.remove(file_path)
        flash(f"File {filename} deleted successfully.", "success")
    except Exception as e:
        flash(f"Error deleting file {filename}: {str(e)}", "error")
    return redirect(url_for('main.list_files'))

@login_required
@main.route('/upload', methods=['GET','POST'])
def upload_dor_file():
    return handle_file_upload(request, UPLOAD_FOLDER, PUBLIC_FOLDER)

@login_required
@main.route('/export/<int:report_id>')
def export_report(report_id):
    report = DORReport.query.get_or_404(report_id)
    pdf_path = export_report_to_pdf(report, UPLOAD_FOLDER)
    return f"PDF generated successfully! <a href='/download/{os.path.basename(pdf_path)}'>Download PDF</a>"