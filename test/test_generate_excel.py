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

    # Test case for multiple user data entries
    assert sheet['A4'].value == 'janet.weaver@reqres.in'
    assert sheet['B4'].value == 'Janet'
    assert sheet['C4'].value == 'Weaver'
    # Add more assertions for additional user data entries

    # Test case for missing user data fields
    assert sheet['A5'].value == 'emma.wong@reqres.in'
    assert sheet['B5'].value == 'Emma'
    assert sheet['C5'].value == 'Wong'
    # Add more assertions for missing user data fields

    # Test case for special characters in user data
    assert sheet['A6'].value == 'user1@example.com'
    assert sheet['B6'].value == 'User with Special Characters'
    assert sheet['C6'].value == 'Special äëñ characters'
    # Add more assertions for user data with special characters

    # Test case for large amount of user data
    assert sheet['A7'].value == 'user1@example.com'
    assert sheet['B7'].value == 'User1'
    assert sheet['C7'].value == 'Lastname1'
    # Add more assertions for large amount of user data

    # Test case for unexpected data types
    assert sheet['A8'].value == 'charles.morris@reqres.in'
    assert sheet['B8'].value == 12345  # Unexpected data type: number instead of a first name
    assert sheet['C8'].value == 'Morris'
    # Add more assertions for user data with unexpected data types

    # Clean up the generated Excel file
    os.remove('user_data.xlsx')
