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

def send_email(recipient:Recipient):
    if recipient.mail_sent_date != '':
        print("{:<30} - {:<30} --> Already been contacted at {}".format(
            recipient.company_name, recipient.email, recipient.mail_sent_date))
        return

    # email details
    send_from = Constants.sender_email
    password = Constants.password
    email_subject = Constants.subject
    email_to = recipient.email
    email_body = Constants.body.replace('in your company', f'at {recipient.company_name}')

    # create message object
    msg = MIMEMultipart()
    msg['From'] = Constants.sender_name
    msg['To'] = email_to
    msg['Subject'] = email_subject

    # attach body to message
    msg.attach(MIMEText(email_body, 'plain'))

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
    try:
        # DANGEROUS !!
        smtp_server.sendmail(send_from, recipient.email, msg.as_string())
        # DANGEROUS !!
        print("{:<30} - {:<30} --> Successfully sent".format(
            recipient.company_name, recipient.email))
        recipient.mail_sent_date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    except Exception as e:
        print(f'{recipient.company_name} - {recipient.email} --> Error! Couldn\'t send.')
        print("{:<30} - {:<30} --> Error! Couldn\'t send".format(
            recipient.company_name, recipient.email))
    smtp_server.quit()
