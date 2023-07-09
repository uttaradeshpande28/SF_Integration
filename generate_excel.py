import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os

print("Fetching user data from the API...")
response = requests.get('https://reqres.in/api/users')
print("response fetched successfully:")
user_data = response.json().get('data', [])
print("User data fetched successfully:")
print(user_data)

print("Creating an Excel workbook...")
wb = Workbook()
sheet = wb.active

print("Writing headers to the Excel sheet...")
sheet['A1'] = 'User Data'
sheet['A2'] = 'Email'
sheet['B2'] = 'First Name'
sheet['C2'] = 'Last Name'
sheet['D2'] = 'Avatar'

print("Writing user data to the Excel sheet...")
for idx, user in enumerate(user_data, start=3):
    sheet[f'A{idx}'] = user['email']
    sheet[f'B{idx}'] = user['first_name']
    sheet[f'C{idx}'] = user['last_name']
    img = Image(user['avatar'])
    sheet.column_dimensions['D'].width = 20
    sheet.row_dimensions[idx].height = 100
    sheet.add_image(img, f'D{idx}')

print("Saving the Excel file...")
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'user_data.xlsx')
wb.save(file_path)
print("Excel file saved at:", file_path)

print("Contents of the current directory:")
print(os.listdir())
