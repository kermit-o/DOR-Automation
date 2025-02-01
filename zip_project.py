import os
import zipfile

def zip_project(project_dir, output_filename, exclude_dirs=None):
    """
    Compress the project directory into a zip file, excluding specified directories.

    :param project_dir: The path to the project directory to compress.
    :param output_filename: The name of the output zip file.
    :param exclude_dirs: A list of directory names to exclude from the zip file.
    """
    exclude_dirs = exclude_dirs or []
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_dir):
            # Exclude specified directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, project_dir)
                zipf.write(file_path, arcname)
    print(f"Project compressed successfully into {output_filename}")

# Specify your project directory and output file name
project_dir = "/workspaces/DOR-Automation"
output_filename = "DOR-Automation.zip"

# Exclude 'venv' directory
exclude_dirs = ["venv"]

zip_project(project_dir, output_filename, exclude_dirs)
