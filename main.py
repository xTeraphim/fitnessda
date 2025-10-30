import csv
import gspread
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
load_dotenv()

LOCAL_CSV = "credentials//sample_data.csv"
SHEET_KEY = os.getenv("SHEET_KEY")

def fetch_sheet(sheet_id: str, creds_file: str = "credentials/credentials.json"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(SHEET_KEY).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

sheet_id = "YOUR_SHEET_ID"
df = fetch_sheet(sheet_id)

print("Headers:", df.columns.tolist())
print(df.head())

def update_local_csv():
    df = fetch_sheet()
    
    # Check if CSV exists
    if os.path.exists(LOCAL_CSV):
        local_df = pd.read_csv(LOCAL_CSV)
        
        # Compare dataframes; if different, overwrite CSV
        if not df.equals(local_df):
            df.to_csv(LOCAL_CSV, index=False)
            print("Local CSV updated from Google Sheet.")
        else:
            print("No changes detected in Google Sheet.")
    else:
        # If CSV does not exist, create it
        df.to_csv(LOCAL_CSV, index=False)
        print("Local CSV created from Google Sheet.")
    
    return df