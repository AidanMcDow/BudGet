import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

edit = 0
stay = 0
add = 0

def addBudGet():
    #Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]
    file_name = './venv/include/client_secret.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
    client = gspread.authorize(creds)

    sheet = client.open('Budget').sheet1
    python_sheet = sheet.get_all_records()
    pp = pprint.PrettyPrinter()
    pp.pprint(python_sheet)


    add = int(input())

    cell = sheet.cell(7,2)
    print('Cell Before Update: ',cell.value)

    sheet.update_cell(7,2,(int(cell.value) + add))
    cell = sheet.cell(7,2)
    print('Cell After Update: ',cell.value)