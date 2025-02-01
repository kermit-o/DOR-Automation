from datetime import datetime
from DORProject.app.models_backup import DORReport
from app import db

def update_database(data, filename):
    for item in data:
        try:
            item['filename'] = filename
            print(f"Processing item: {item}")

            existing_record = db.session.query(DORReport).filter_by(filename=item['filename']).first()
            if existing_record:
                existing_record.processed_data = item.get('text', existing_record.processed_data)
                existing_record.upload_date = datetime.utcnow()
                db.session.commit()
            else:
                new_report = DORReport(
                    filename=item['filename'],
                    upload_date=datetime.utcnow(),
                    processed_data=item.get('text', '')
                )
                db.session.add(new_report)
                db.session.commit()
        except Exception as e:
            print(f"Error updating database record: {str(e)}")