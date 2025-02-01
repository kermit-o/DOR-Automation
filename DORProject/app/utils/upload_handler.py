import os
import datetime
from flask import flash, redirect, url_for
from ..utils.file_utils import generate_unique_filename
from ..utils.file_handler import detect_file_type
from ..utils.xml_handler import extract_data_from_xml
from ..utils.update_dor import update_dor_template

def handle_file_upload(request, upload_folder, public_folder):
    """Maneja la subida y procesamiento de archivos DOR y XML"""

    if 'template_file' not in request.files or 'data_files' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('main.index'))

    template_file = request.files['template_file']
    data_files = request.files.getlist('data_files')

    if template_file.filename == '':
        flash('No selected template file', 'error')
        return redirect(url_for('main.index'))

    uploaded_files = []
    xml_files = []

    # 🔹 Guardar el archivo DOR
    filename = template_file.filename
    file_type = detect_file_type(filename)

    if file_type != "DOR":
        flash(f"Unsupported template file format: {filename}. Please upload a valid DOR file (.xlsx/.xlsm)", 'error')
        return redirect(url_for('main.index'))

    unique_filename = generate_unique_filename(upload_folder, filename)
    template_file_path = os.path.join(upload_folder, unique_filename)
    template_file.save(template_file_path)
    uploaded_files.append(template_file_path)

    # 🔹 Guardar los archivos XML y validar su contenido
    extracted_data_list = []
    forecast_data = {}

    current_date = datetime.datetime.today()
    expected_months = [
        current_date.strftime("%Y-%m"),  # Mes actual
        (current_date + datetime.timedelta(days=32)).strftime("%Y-%m"),  # Próximo mes
        (current_date + datetime.timedelta(days=64)).strftime("%Y-%m"),  # +2 meses
        (current_date + datetime.timedelta(days=96)).strftime("%Y-%m")   # +3 meses
    ]

    for file in data_files:
        filename = file.filename
        if filename == '':
            continue

        file_type = detect_file_type(filename)
        if file_type != "XML":
            flash(f"Unsupported data file format: {filename}. Please upload XML files.", 'error')
            return redirect(url_for('main.index'))

        unique_filename = generate_unique_filename(upload_folder, filename)
        file_path = os.path.join(upload_folder, unique_filename)
        file.save(file_path)

        # Extraer datos y determinar su fecha
        extracted_data = extract_data_from_xml(file_path)
        forecast_date = extracted_data.get("forecast_date", "N/A")[:7]  # Extraer solo "YYYY-MM"

        if forecast_date in expected_months:
            forecast_data[forecast_date] = extracted_data
        else:
            flash(f"Error: XML file {filename} does not match the expected forecast months.", 'error')
            return redirect(url_for('main.index'))

    # 🔹 Verificar si tenemos exactamente los cuatro archivos requeridos
    if len(forecast_data) != 4:
        flash('Error: You must upload 4 XML data files corresponding to the expected months.', 'error')
        return redirect(url_for('main.index'))

    # 🔹 Ordenar los archivos en la lista en el orden correcto (actual, +1, +2, +3 meses)
    extracted_data_list = [forecast_data[month] for month in expected_months]

    # 🔹 Actualizar la plantilla DOR con los datos extraídos
    updated_file_path = update_dor_template(template_file_path, extracted_data_list)

    flash('Files uploaded and processed successfully!', 'success')
    return redirect(url_for('main.download_file', filename=os.path.basename(updated_file_path)))
