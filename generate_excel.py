import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Fetch user data from the API
response = requests.get('https://reqres.in/api/users')
user_data = response.json().get('data', [])

# Create an Excel workbook and sheet
wb = Workbook()
sheet = wb.active

# Write headers
sheet['A1'] = 'User Data'
sheet['A2'] = 'Email'
sheet['B2'] = 'First Name'
sheet['C2'] = 'Last Name'
sheet['D2'] = 'Avatar'

# Write user data to the Excel file
for idx, user in enumerate(user_data, start=3):
    sheet[f'A{idx}'] = user['email']
    sheet[f'B{idx}'] = user['first_name']
    sheet[f'C{idx}'] = user['last_name']
    img = Image(user['avatar'])
    sheet.column_dimensions['D'].width = 20
    sheet.row_dimensions[idx].height = 100
    sheet.add_image(img, f'D{idx}')

# Save the Excel file
wb.save('user_data.xlsx')
