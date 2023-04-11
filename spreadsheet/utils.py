from spreadsheet.sheet import Sheet
from emailer.constants import Constants
from emailer.recipient import Recipient
from typing import List

def get_recipients_from_data(data:List[List[str]]) -> List[Recipient]:
    recipients = []
    for row in data:
        newRecipient = Recipient(
            company_name=row[0],
            email=row[1],
            country=row[2],
            website=row[3],
            mail_sent_date=row[4]
        )
        recipients.append(newRecipient)
    return recipients

def get_data_from_recipients(recipients:List[Recipient]):
    data = []
    for recipient in recipients:
        data.append(list(vars(recipient).values()))
    return data