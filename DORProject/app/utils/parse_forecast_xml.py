import xml.etree.ElementTree as ET

def parse_forecast_xml(file_path):
    """
    Extrae los datos relevantes del archivo XML de Forecast.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Inicializar valores acumulativos
        total_revenue = 0
        total_no_rooms = 0
        total_complimentary_rooms = 0
        total_house_use_rooms = 0
        sumooo_room_per_report = None

        # Recorrer cada entrada relevante en el XML
        for entry in root.findall("DATA_ENTRY"):  # Ajustar etiqueta si es necesario
            total_revenue += float(entry.find("REVENUE").text) if entry.find("REVENUE") is not None else 0
            total_no_rooms += int(entry.find("NO_ROOMS").text) if entry.find("NO_ROOMS") is not None else 0
            total_complimentary_rooms += int(entry.find("COMPLIMENTARY_ROOMS").text) if entry.find("COMPLIMENTARY_ROOMS") is not None else 0
            total_house_use_rooms += int(entry.find("HOUSE_USE_ROOMS").text) if entry.find("HOUSE_USE_ROOMS") is not None else 0

            # Capturar el primer valor de SUMOOO_ROOMSPERREPORT
            if sumooo_room_per_report is None and entry.find("SUMOOO_ROOMSPERREPORT") is not None:
                sumooo_room_per_report = int(entry.find("SUMOOO_ROOMSPERREPORT").text)

        # Construcción del diccionario con los valores extraídos
        data = {
            "REVENUE": total_revenue,
            "NO_ROOMS": total_no_rooms,
            "COMPLIMENTARY_ROOMS": total_complimentary_rooms,
            "HOUSE_USE_ROOMS": total_house_use_rooms,
            "SUMOOO_ROOMSPERREPORT": sumooo_room_per_report if sumooo_room_per_report is not None else 0
        }

        return data

    except ET.ParseError as e:
        print(f"Error al procesar el XML {file_path}: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado en {file_path}: {e}")
        return None
