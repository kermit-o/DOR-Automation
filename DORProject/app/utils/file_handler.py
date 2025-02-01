import os

def detect_file_type(filename):
    """Detecta si el archivo es DOR o XML basado en el nombre"""
    if filename.lower().endswith(".xlsx"):
        return "DOR"
    elif filename.lower().endswith(".xml"):
        return "XML"
    return "UNKNOWN"

def extract_file_category(filename):
    """Extrae la categoría del archivo basándose en el nombre"""
    base_name = filename.split("_")[0].lower()  # Ejemplo: "forecast_65464346.xml" → "forecast"
    return base_name
