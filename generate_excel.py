import requests
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from PIL import Image as PILImage

print("Imports successful.")

def fetch_user_data():
    print("Fetching user data from the API...")
    response = requests.get('https://reqres.in/api/users')
    print("Response fetched successfully:")
    user_data = response.json().get('data', [])
    print("User data fetched successfully:")
    print(user_data)
    return user_data, response

def download_image(url, filename):
    response = requests.get('https://reqres.in/api/users')
    with open(filename, 'wb') as image_file:
        image_file.write(response.content)

def generate_pdf_file():
    user_data, response = fetch_user_data()

    print("Creating a PDF file...")
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'user_data.pdf')
    print("File path:", file_path)
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    elements = []

    # Define table data
    data = [['Email', 'First Name', 'Last Name', 'Avatar']]
    for user in user_data:
        email = user['email']
        first_name = user['first_name']
        last_name = user['last_name']
        avatar_url = user['avatar']
        
        # Download the avatar image
        image_filename = os.path.basename(avatar_url)
        image_path = os.path.join(current_directory, image_filename)
        print("Downloading avatar image:", avatar_url)
        download_image(avatar_url, image_path)
        
        # Add the row to the table data
        data.append([email, first_name, last_name, image_path])
    
    # Create the table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    
    # Add the table to the elements list
    elements.append(table)
    
    # Build the PDF document
    doc.build(elements)
    
    print("PDF file saved as user_data.pdf")

generate_pdf_file()
