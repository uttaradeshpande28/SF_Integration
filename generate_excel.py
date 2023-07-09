import requests
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors

def fetch_user_data():
    response = requests.get('https://reqres.in/api/users')
    data = response.json().get('data', [])
    return data

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as image_file:
        image_file.write(response.content)

def generate_pdf_file():
    user_data = fetch_user_data()

    doc = SimpleDocTemplate("user_data.pdf", pagesize=letter)
    elements = []

    data = [['Email', 'First Name', 'Last Name', 'Avatar']]
    for user in user_data:
        email = user['email']
        first_name = user['first_name']
        last_name = user['last_name']
        avatar_url = user['avatar']

        image_filename = f'{user["id"]}-avatar.jpg'
        download_image(avatar_url, image_filename)

        data.append([email, first_name, last_name, Image(image_filename, width=1.5*inch, height=1.5*inch)])

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

generate_pdf_file()
