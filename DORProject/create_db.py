from sqlalchemy import create_engine, text

# Usa la misma URI que tienes en Flask
engine = create_engine("sqlite:////workspaces/DOR-Automation/DORProject/instance/dor_reports.db")

# Intenta crear una tabla simple
try:
    conn = engine.connect()
    conn.execute(text("CREATE TABLE IF NOT EXISTS test_table (id INTEGER PRIMARY KEY)"))
    conn.close()
    print("Database and table created successfully.")
except Exception as e:
    print("Error:", e)
