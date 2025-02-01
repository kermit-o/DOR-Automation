import os
from file_handler import detect_file_type, extract_file_category
from xml_handler import extract_data_from_xml
from update_dor import update_dor_template

def process_uploaded_files(files):
    dor_file = None
    xml_files = []

    # 🔹 Separar archivos
    for file_path in files:
        file_type = detect_file_type(file_path)
        if file_type == "DOR":
            dor_file = file_path
        elif file_type == "XML":
            xml_files.append(file_path)

    if not dor_file or len(xml_files) < 4:
        raise ValueError("Faltan archivos. Se necesita 1 DOR y 4 XML.")

    # 🔹 Extraer datos de los XML
    extracted_data_list = []
    for xml in xml_files:
        extracted_data_list.append(extract_data_from_xml(xml))

    # 🔹 Actualizar la plantilla DOR con los datos extraídos
    updated_dor_path = update_dor_template(dor_file, extracted_data_list)
    
    return updated_dor_path
