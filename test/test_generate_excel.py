import os
from openpyxl import load_workbook
import pytest
from openpyxl.drawing.image import Image as ExcelImage

print("Imports successful test file")

def test_generate_excel_file():
    # Generate the Excel file
    exec(open("generate_excel.py").read())

    # Verify the contents of the current directory
    print("Contents of the current directory:")
    print(os.listdir())

    # Verify that the Excel file is generated successfully
    assert os.path.exists('user_data.xlsx')

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

    # Verify the image file
    # cell_with_image = sheet['D3']
    # image_filename = os.path.basename(cell_with_image.value)
    # image_path = os.path.join(os.getcwd(), image_filename)

    img = sheet['D3'].image
    assert img.width_cm == 3.39
    assert img.height_cm == 3.39

    # Verify the image file format
    assert img.format == 'jpeg'

    # Verify the cleanup of the local image file
    assert not os.path.exists('1-image.jpg')

    # Clean up the generated Excel file
    os.remove('user_data.xlsx')
