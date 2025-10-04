import os
import shutil
import subprocess
import zipfile

# --- Configuration ---
PROJECT_NAME = "MyPythonApp"
SOURCE_DIR = "src"  # Directory containing your Python source code
BUILD_DIR = "build"  # Directory for build artifacts
DIST_DIR = "dist"    # Directory for distributable packages
DEPLOY_TARGET_DIR = "/var/www/html/my_app" # Example deployment target


def create_package():
    """Creates a distributable package (e.g., a zip file). but  depend on database for an path """
    # connecyting data base and from  getting dict dir
    print("Creating distributable package...")
    package_name = f"{PROJECT_NAME}_v1.0.0.zip"  # Example versioning
    package_path = os.path.join(DIST_DIR, package_name)

    with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(SOURCE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, SOURCE_DIR)
                zipf.write(file_path, arcname)
    print(f"Package created: {package_path}")
    return package_path
