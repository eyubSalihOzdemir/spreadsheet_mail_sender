import google.auth
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class Sheet:
    def __init__(self, spreadsheet_id):
        self.creds = Credentials.from_service_account_file('key.json')
        self.service = build('sheets', 'v4', credentials=self.creds)
        self.spreadsheet_id = spreadsheet_id

    def read(self, range_name):
        result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range=range_name).execute()
        return result.get('values', [])

    def write(self, range_name, values):
        body = {
            'values': values
        }
        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id, range=range_name,
            valueInputOption='USER_ENTERED', body=body).execute()

    def send_email_to_recipients(sheet, recipients_range):
        recipients = sheet.read(recipients_range)
        for recipient_row in recipients:
            company_name = recipient_row[0]
            email = recipient_row


