import smtplib
from typing import List
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
from emailer.constants import Constants
from emailer.recipient import Recipient
from datetime import datetime

def send_email(recipients:List[Recipient]):
    # email details
    send_from = Constants.sender_email
    subject = Constants.subject
    body = Constants.body
    password = Constants.password

    # create message object
    msg = MIMEMultipart()
    msg['From'] = Constants.sender_name
    msg['Subject'] = subject

    # attach body to message
    msg.attach(MIMEText(body, 'plain'))

    # attachment details
    attachments = {
        Constants.resume_path: Constants.resume_name,
        Constants.cover_letter_path : Constants.cover_letter_name
    }

    # attach file to message
    for attachment_path in attachments.keys():
        attachment_name = attachments[attachment_path]

        with open(attachment_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=attachment_name)
            msg.attach(part)

    # send message
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(send_from, password)
    for recipient in recipients:
        msg['To'] = recipient.email
        try:
            # DANGEROUS !!
            #smtp_server.sendmail(send_from, recipient.email, msg.as_string())
            # DANGEROUS !!
            print(f'{recipient.company_name} - {recipient.email} --> Successfully sent')
            recipient.mail_sent_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        except Exception as e:
            print(f'{recipient.company_name} - {recipient.email} --> Error! Couldn\'t send.')
    smtp_server.quit()
