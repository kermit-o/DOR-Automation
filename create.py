import os

def create_project_structure(base_dir):
    # Define la estructura del proyecto
    structure = {
        "app": ["__init__.py", "routes.py", "models.py"],
        "static": [],
        "templates": [],
        "tests": ["test_app.py"],
        "": ["requirements.txt", ".gitignore", "README.md"]
    }

    # Crea los directorios y archivos
    for folder, files in structure.items():
        folder_path = os.path.join(base_dir, folder)
        if folder:
            os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w") as f:
                if file == "requirements.txt":
                    f.write("Flask\npandas\nopenpyxl\nPyPDF2\n")
                elif file == ".gitignore":
                    f.write("__pycache__/\n*.pyc\n*.pyo\n.env\n*.sqlite3\n")
                elif file == "README.md":
                    f.write("# DOR Automation Project\n\nAutomate DOR report generation.")

# Ejecuta el script
if __name__ == "__main__":
    base_dir = input("Enter the base directory for your project: ").strip()
    if not base_dir:
        base_dir = os.getcwd()

    create_project_structure(base_dir)
    print(f"Project structure created successfully in {base_dir}")
