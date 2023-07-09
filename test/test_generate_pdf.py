import os
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

def test_delete_existing_images():
    # Create temporary .jpg files in the workspace
    test_files = ["test1.jpg", "test2.jpg", "test3.png"]
    workspace_path = os.getcwd()
    for file_name in test_files:
        with open(os.path.join(workspace_path, file_name), "w"):
            pass
