import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('IMS')

inventory = SHEET.worksheet('inventory')

data = inventory.get_all_values()



def role_manager():
    print("Congrats you are a manager")


def role_supervisor():
    print("Congrats you are a supervisor")


def role_assisstant():
    print("Congrats you are a shop assisstant")


def add_stock():
    print("stock added")

def view_stock():
    print(data)

def edit_stock():
    print("What item would you like to edit?")


def remove_stock():
    print("What item would you like to remove")

role_manager()

role_supervisor()

role_assisstant()

add_stock()

view_stock()

edit_stock()

remove_stock()