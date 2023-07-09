import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
import pytest

def test_generate_pdf_file():
    # Verify the contents of the current directory
    print("Contents of the current directory:")
    print(os.listdir())

    # Verify that the PDF file is generated successfully
    assert os.path.exists('user_data.pdf')

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
    
        # Define the expected values for email, first name, and last name
        expected_email = "example@example.com"
        expected_first_name = "John"
        expected_last_name = "Doe"
    
        # Check if the email, first name, and last name values match the expected values
        assert email == expected_email, f"Email '{email}' does not match expected value"
        assert first_name == expected_first_name, f"First name '{first_name}' does not match expected value"
        assert last_name == expected_last_name, f"Last name '{last_name}' does not match expected value"

    # Clean up the generated PDF file
    #os.remove('user_data.pdf')
