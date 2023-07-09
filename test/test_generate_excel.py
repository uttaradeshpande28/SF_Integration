import os
from openpyxl import load_workbook
import pytest
print("Imports successful test file")

def test_generate_excel_file():
    # Verify the contents of the current directory
    print("Contents of the current directory _test:")
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

    # Clean up the generated Excel file
    os.remove('user_data.xlsx')
