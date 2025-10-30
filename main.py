import gspread
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
load_dotenv()
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
    return df

sheet_id = "YOUR_SHEET_ID"
df = fetch_sheet(sheet_id)

print("Headers:", df.columns.tolist())
print(df.head())

df.plot(kind="line")
plt.show()