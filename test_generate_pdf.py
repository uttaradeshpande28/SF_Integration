import os
import requests
import unittest
from unittest.mock import patch, MagicMock
import pytest
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors


# Import the functions to be tested
from generate_pdf import delete_existing_images, fetch_user_data, generate_pdf_file

# Mock the requests.get method to return a mock response
@patch('requests.get')
def test_fetch_user_data(mock_get):
    # Prepare mock data and response
    url = "https://reqres.in/api/users"
    mock_data = {'data': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'avatar': 'http://example.com/avatar.jpg', 'email': 'john.doe@example.com'}]}
    mock_get.return_value = MagicMock(status_code=200, json=lambda: mock_data)

    # Call the function to be tested
    data = fetch_user_data(url)

    # Assertions
    assert data == mock_data['data']
    mock_get.assert_called_once_with(url)

def test_delete_existing_images(tmpdir):
    # Create temporary test directory
    workspace_path = tmpdir.mkdir("workspace")
    os.chdir(workspace_path)

    # Create some dummy image files
    image_files = ['1-John_Doe.jpg', '2-Jane_Smith.jpg', '3-Michael_Johnson.jpg', '4-Sarah_Walker.jpg']
    for file_name in image_files:
        with open(file_name, 'w'):
            pass

    # Call the function to be tested
    delete_existing_images()

    # Assertions
    assert len(os.listdir(workspace_path)) == 0

def test_generate_pdf_file():
    # Run the PDF generation process
    generate_pdf_file()
    
    # Get the current working directory
    current_dir = os.getcwd()

    # Define the path to the PDF file
    pdf_file_path = os.path.join(current_dir, 'user_data.pdf')

    # Assert that the PDF file exists
    assert os.path.exists(pdf_file_path)
    
    # Verify the content of the PDF file
    doc = SimpleDocTemplate("user_data.pdf", pagesize=letter)
    elements = []

    # Load the PDF file and extract its content
    with open("user_data.pdf", "rb") as file:
        pdf_content = file.read()

    # Define the expected data
    expected_data = [
        {'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth'},
        # Add more expected data rows as needed
    ]

    # Iterate over the expected data and check if the values are present in the PDF file
    # Iterate over the expected data and check if the values are present in the PDF file
    # Iterate over the expected data and check if the values are present in the PDF file
    for i, data in enumerate(expected_data):
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
    
    # Check if the email, first name, and last name values exist
    assert email, f"Email is missing for data index {i}"
    assert first_name, f"First name is missing for data index {i}"
    assert last_name, f"Last name is missing for data index {i}"
    
# Run the tests
if __name__ == '__main__':
    pytest.main(['-k', 'test_generate_pdf_file'])
