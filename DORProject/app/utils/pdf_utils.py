import os
import json
from reportlab.pdfgen import canvas
import PyPDF2

def extract_data_from_pdf(file_path):
    data = []
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if not reader.pages:
                print(f"No pages found in PDF: {file_path}")
                return None
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    data.append({"filename": os.path.basename(file_path), "text": text})
                else:
                    print(f"No text found on page {reader.pages.index(page) + 1} of PDF: {file_path}")
        return data if data else None
    except Exception as e:
        print(f"Error reading PDF file {file_path}: {str(e)}")
        return None

def export_report_to_pdf(report, upload_folder):
    pdf_path = os.path.join(upload_folder, f"report_{report.id}.pdf")
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 800, f"Report ID: {report.id}")
    c.drawString(100, 780, f"Filename: {report.filename}")
    c.drawString(100, 760, f"Upload Date: {report.upload_date}")
    c.drawString(100, 740, "Processed Data:")

    y_position = 720
    data = json.loads(report.processed_data)
    for row in data:
        c.drawString(100, y_position, str(row))
        y_position -= 20
        if y_position < 50:
            c.showPage()
            y_position = 800

    c.save()
    return pdf_path