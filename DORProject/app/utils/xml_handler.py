import xml.etree.ElementTree as ET

def extract_data_from_xml(file_path):
    """Lee un archivo XML y extrae los valores necesarios"""
    tree = ET.parse(file_path)
    root = tree.getroot()

    data = {
        "REVENUE": root.find("REVENUE").text if root.find("REVENUE") else "0",
        "NO_ROOMS": root.find("NO_ROOMS").text if root.find("NO_ROOMS") else "0",
        "COMPLIMENTARY_ROOMS": root.find("COMPLIMENTARY_ROOMS").text if root.find("COMPLIMENTARY_ROOMS") else "0",
        "HOUSE_USE_ROOMS": root.find("HOUSE_USE_ROOMS").text if root.find("HOUSE_USE_ROOMS") else "0",
        "SUMOOO_ROOMSPERREPORT": root.find("SUMOOO_ROOMSPERREPORT").text if root.find("SUMOOO_ROOMSPERREPORT") else "0"
    }

    return data
