import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os
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

def generate_excel_file():
    user_data, response = fetch_user_data()

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
    idx_values = []  # Declare an empty list to store idx values
    idx_value = ''  # Declare the variable outside the loop
    for idx, user in enumerate(user_data, start=3):
        sheet[f'A{idx}'] = user['email']
        sheet[f'B{idx}'] = user['first_name']
        sheet[f'C{idx}'] = user['last_name']
        avatar_url = user['avatar']
        image_filename = os.path.basename(avatar_url)
        image_path = os.path.join(os.getcwd(), image_filename)
        response = requests.get(avatar_url)
        with open(image_path, 'wb') as image_file:
            image_file.write(response.content)
        img = Image(image_path)
        sheet.column_dimensions['D'].width = 20
        sheet.row_dimensions[idx].height = 100
        sheet.add_image(img, f'D{idx}')
        
        # Add the idx value to the list
        idx_values.append(idx)
    
    print("Saving the Excel file...")
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'user_data.xlsx')
    wb.save(file_path)
    print("Excel file saved at:", file_path)
    
    print("Contents of the current directory:")
    print(os.listdir())

    return idx_values  # Return the list of idx values
