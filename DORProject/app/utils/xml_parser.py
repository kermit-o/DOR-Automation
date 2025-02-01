import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_file):
    """Extrae los valores de las etiquetas relevantes de un archivo XML."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = {
        "REVENUE": root.find("REVENUE").text if root.find("REVENUE") is not None else "0",
        "NO_ROOMS": root.find("NO_ROOMS").text if root.find("NO_ROOMS") is not None else "0",
        "COMPLIMENTARY_ROOMS": root.find("COMPLIMENTARY_ROOMS").text if root.find("COMPLIMENTARY_ROOMS") is not None else "0",
        "HOUSE_USE_ROOMS": root.find("HOUSE_USE_ROOMS").text if root.find("HOUSE_USE_ROOMS") is not None else "0",
        "SUMOOO_ROOMSPERREPORT": root.find("SUMOOO_ROOMSPERREPORT").text if root.find("SUMOOO_ROOMSPERREPORT") is not None else "0"
    }
    
    return data
