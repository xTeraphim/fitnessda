import gspread
import pandas as pd
import matplotlib.pyplot as plt

from oauth2client.service_account import ServiceAccountCredentials

def fetch_sheet(sheet_id: str, creds_file: str = "credentials.json"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key('1lfhUR8BMkGZBUQVZweY3joVVpSgarU5Febq04lEOWtY').sheet1
    df = fetch_sheet("YOUR_SHEET_ID")
    print(df.head())
    return sheet.get_all_records()