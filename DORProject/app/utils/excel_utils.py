import os
import shutil
from openpyxl import load_workbook
from datetime import datetime
import pandas as pd
from .data_utils import process_uploaded_files

def update_template_with_data(template_path, data_files, public_folder):
    # Procesar los datos de los archivos subidos
    data_frames = process_uploaded_files(data_files)

    workbook = load_workbook(template_path, keep_vba=True)
    sheet = workbook['Set-up']

    # Actualizar la fecha en la celda D2
    sheet['D2'] = datetime.now().strftime('%Y-%m-%d')

    # Función para actualizar las celdas específicas
    def update_cells(sheet, data, column_letter):
        sum_no_rooms = data['NO_ROOMS'].sum()
        sum_revenue = data['REVENUE'].sum()
        
        try:
            sumoo_rooms = data.loc[1, 'SUMOOO_ROOMSPERREPORT']
        except KeyError:
            sumoo_rooms = 0
            print(f"Column 'SUMOOO_ROOMSPERREPORT' not found in the data for column {column_letter}")
        except IndexError:
            sumoo_rooms = 0
            print(f"Row 2 not found for column 'SUMOOO_ROOMSPERREPORT' in column {column_letter}")

        sum_complimentary_rooms = data['COMPLIMENTARY_ROOMS'].sum()

        sheet[f'{column_letter}6'] = sum_no_rooms
        sheet[f'{column_letter}8'] = sum_revenue
        sheet[f'{column_letter}10'] = sumoo_rooms
        sheet[f'{column_letter}11'] = sum_complimentary_rooms
        sheet[f'{column_letter}12'] = sum_complimentary_rooms

        for i in range(6, 13):
            sheet[f'{column_letter}{i + 10}'] = sheet[f'{column_letter}{i}'].value

    # Actualizar las celdas para cada archivo y columna
    update_cells(sheet, data_frames[data_files[0]], 'C')
    update_cells(sheet, data_frames[data_files[1]], 'D')
    update_cells(sheet, data_frames[data_files[2]], 'E')
    update_cells(sheet, data_frames[data_files[3]], 'F')

    updated_file_path = os.path.join(os.path.dirname(template_path), 'updated_template.xlsx')
    workbook.save(updated_file_path)
    
    # Mover el archivo a la carpeta pública
    public_file_path = os.path.join(public_folder, 'updated_template.xlsx')
    shutil.move(updated_file_path, public_file_path)
    print(f"Updated template moved to {public_file_path}")
    
    return public_file_path