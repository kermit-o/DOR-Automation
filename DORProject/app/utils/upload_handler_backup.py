import os
from flask import flash, redirect, url_for
from ..utils.file_utils import generate_unique_filename
from ..utils.excel_utils import update_template_with_data


def handle_file_upload(request, upload_folder, public_folder):
    if 'template_file' not in request.files or 'data_files' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('main.index'))

    template_file = request.files['template_file']
    data_files = request.files.getlist('data_files')

    if template_file.filename == '':
        flash('No selected template file', 'error')
        return redirect(url_for('main.index'))

    uploaded_files = []

    # Guardar el archivo de plantilla
    filename = template_file.filename
    if '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ['xlsx', 'xlsm']:
        flash(f"Unsupported file format: {filename}. Please upload a .xlsx or .xlsm file.", 'error')
        return redirect(url_for('main.index'))

    unique_filename = generate_unique_filename(upload_folder, filename)
    template_file_path = os.path.join(upload_folder, unique_filename)
    template_file.save(template_file_path)
    uploaded_files.append(template_file_path)

    # Guardar los archivos de datos
    data_file_paths = []
    for file in data_files:
        filename = file.filename
        if filename == '':
            continue
        if '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ['xlsx', 'xlsm', 'csv']:
            flash(f"Unsupported file format: {filename}. Please upload a .xlsx, .xlsm, or .csv file.", 'error')
            return redirect(url_for('main.index'))

        unique_filename = generate_unique_filename(upload_folder, filename)
        file_path = os.path.join(upload_folder, unique_filename)
        file.save(file_path)
        data_file_paths.append(file_path)

    updated_file_path = update_template_with_data(template_file_path, data_file_paths, public_folder)
    flash('Files uploaded and processed successfully!', 'success')
    return redirect(url_for('main.download_file', filename=os.path.basename(updated_file_path)))