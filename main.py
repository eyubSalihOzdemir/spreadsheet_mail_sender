from emailer.sender import send_email
from emailer.recipient import Recipient
from emailer.constants import Constants
from spreadsheet.sheet import Sheet
from spreadsheet.utils import *
import spreadsheet.utils

if __name__ == '__main__':
    # Read data from spreadsheet
    sheet = Sheet(Constants.spreadsheet_id)
    data = sheet.read('Sheet1!A2:F')

    # Get Recipient objects from data
    recipients = get_recipients_from_data(data)

    # Send email to recipients
    send_email(recipients)

    # Write data to spreadsheet, because 'Mail Sent' field might have changed
    data = get_data_from_recipients(recipients)
    sheet.write('Sheet1!A2:F', data)


# 1. Create a project on Google Cloud console
# 2. Create a service account
# 3. Create a JSON key for that service account and save it locally (edit path in emailer/constants.py)
# 4. Share your Google Sheet with service account email address
# 5. Extract sheet id from your sheets URL and save it locally (edit in emailer/constants.py)
# 6. From Google Account/Security settings, create a 16-digit App Password for your email and save it locally (edit in emailer/constants.py)