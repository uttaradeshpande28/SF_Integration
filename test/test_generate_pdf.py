import os
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

def test_fetch_user_data():
    # Define test data
    url = "https://reqres.in/api/users"

    # Call the fetch_user_data function
    data = fetch_user_data(url)

    # Assert that the data is fetched successfully
    assert isinstance(data, list), "Data is not a list"
    assert len(data) > 0, "No data fetched"

def test_generate_pdf_file():
    # Define test data
    user_data = [
        {'email': 'example1@example.com', 'first_name': 'John', 'last_name': 'Doe', 'avatar': 'https://example.com/avatar1.jpg'},
        {'email': 'example2@example.com', 'first_name': 'Jane', 'last_name': 'Smith', 'avatar': 'https://example.com/avatar2.jpg'}
    ]

    # Call the generate_pdf_file function
    generate_pdf_file(user_data)

    # Assert that the PDF file is generated successfully
    pdf_path = os.path.join(os.getcwd(), "user_data.pdf")
    assert os.path.exists(pdf_path), f"PDF file '{pdf_path}' does not exist"
    assert os.path.getsize(pdf_path) > 0, f"PDF file '{pdf_path}' is empty"

# Run the tests
test_fetch_user_data()
test_generate_pdf_file()
