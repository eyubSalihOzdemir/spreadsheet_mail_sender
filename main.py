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