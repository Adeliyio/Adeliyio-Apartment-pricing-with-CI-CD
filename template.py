import os
from pathlib import Path
import logging

# Configure logging to display timestamp and message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the project name
project_name = "mlProject"

# List of directories and files to create for the project setup
list_of_files = [
    # GitHub Actions workflow directory placeholder
    ".github/workflows/.gitkeep",
    
    # Source directories and initialization files
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    
    # Configuration and other essential files
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    
    # Research and template files
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# Iterate over the list of file paths
for filepath in list_of_files:
    # Convert string path to a Path object for better handling
    filepath = Path(filepath)
    
    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)

    # Check if a directory is specified, then create it if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't already exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file does not exist or is empty, then create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log a message if the file already exists and is not empty
        logging.info(f"{filename} already exists")
