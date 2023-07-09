import os
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

def delete_existing_images():
    """
    Delete existing .jpg files in the workspace.
    """
    workspace_path = os.getcwd()
    for file_name in os.listdir(workspace_path):
        if file_name.endswith(".jpg"):
            os.remove(os.path.join(workspace_path, file_name))

def fetch_user_data(url):
    """
    Fetch user data from the API.
    """
    response = requests.get(url)
    data = response.json().get('data', [])
    return data

def generate_pdf_file():
    """
    Generate a PDF file with user data and avatar images.
    """
    api_url = "https://reqres.in/api/users"
    delete_existing_images()

    # Fetch user data from the API
    user_data = fetch_user_data(api_url)
    image_filenames = []

    # Download avatar images and save in the workspace
    for user in user_data:
        avatar_url = user['avatar']
        image_filename = f'{user["id"]}-{user["first_name"]}_{user["last_name"]}.jpg'
        response = requests.get(avatar_url)
        with open(os.path.join(os.getcwd(), image_filename), 'wb') as image_file:
            image_file.write(response.content)
        
        image_filenames.append(image_filename)

    # Create PDF document
    doc = SimpleDocTemplate("user_data.pdf", pagesize=letter)
    elements = []

    data = [['Email', 'First Name', 'Last Name', 'Avatar']]
    for user, image_filename in zip(user_data, image_filenames):
        email = user['email']
        first_name = user['first_name']
        last_name = user['last_name']
        avatar_image = Image(os.path.join(os.getcwd(), image_filename), width=50, height=50)
        data.append([email, first_name, last_name, avatar_image])

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

    elements.append(table)

    doc.build(elements)
