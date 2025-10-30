import gspread
import pandas as pd
import matplotlib.pyplot as plt

from oauth2client.service_account import ServiceAccountCredentials

def fetch_sheet(sheet_id: str, creds_file: str = "credentials/credentials.json"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key('1lfhUR8BMkGZBUQVZweY3joVVpSgarU5Febq04lEOWtY').sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df   # function ends here

# --- code below runs the function ---
sheet_id = "YOUR_SHEET_ID"
df = fetch_sheet(sheet_id)

print("Headers:", df.columns.tolist())
print(df.head())

df.plot(kind="line")
plt.show()