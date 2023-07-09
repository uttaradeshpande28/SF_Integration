import os
from openpyxl import load_workbook
import pytest
from openpyxl.drawing.image import Image
from openpyxl.drawing.image import Image as ExcelImage
from generate_excel import fetch_user_data
from generate_excel import generate_excel_file

print("Imports successful test file")

def test_generate_excel_file():
    user_data, response = fetch_user_data()
    # Verify the user data
    assert len(user_data) > 0  # Check if user data is not empty
    # verifu response status
    assert response.status_code == 200
    
    # Generate the Excel file
    exec(open("generate_excel.py").read())

    # Verify the contents of the current directory
    print("Contents of the current directory:")
    print(os.listdir())

    # Verify that the Excel file is generated successfully
    assert os.path.exists('user_data.xlsx')

    # Generate the Excel file
    generate_excel_file()
    
    # Verify the contents of the Excel file
    workbook = load_workbook('user_data.xlsx')
    sheet = workbook.active

    # Verify the headers and user data
    assert sheet['A1'].value == 'User Data'
    assert sheet['A2'].value == 'Email'
    assert sheet['B2'].value == 'First Name'
    assert sheet['C2'].value == 'Last Name'
    assert sheet['D2'].value == 'Avatar'

    # Verify the user data
    assert sheet['A3'].value == 'george.bluth@reqres.in'
    assert sheet['B3'].value == 'George'
    assert sheet['C3'].value == 'Bluth'

    # Generate the Excel file
    idx_values = generate_excel_file()

    # Verify the image data in specific cells
    for idx_value in idx_values:
        cell_with_image = sheet[f'D{idx_value}']
        image = cell_with_image.value
        # Check if the cell value is not None
        assert image is not None
    
    # Verify the image file
    # cell_with_image = sheet['D3']
    # image_filename = os.path.basename(cell_with_image.value)
    # image_path = os.path.join(os.getcwd(), image_filename)

    #img = sheet['D3'].avatar
    #assert img.width_cm == 3.39
    #assert img.height_cm == 3.39

    # Verify the image file format
    #assert img.format == 'jpeg'

    # Clean up the generated Excel file
    os.remove('user_data.xlsx')
