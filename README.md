## spreadsheet_mail_sender
This projects collects a set of information from a Google Spreadsheet and then sends multiple emails to addresses in that information. You might need to make
some few changes to the code in order to fit your use case like spreadsheet ranges, object models, config files etc.

# Basic steps
1. Create a project on Google Cloud console
2. Create a service account
3. Create a JSON key for that service account and save it locally (edit path in emailer/constants.py)
4. Enable Google Spreadsheet API for your project
5. Share your Google Sheet with service account email address
6. Extract sheet id from your sheets URL and save it locally (edit in emailer/constants.py)
7. From Google Account/Security settings, create a 16-digit App Password for your email and save it locally (edit in emailer/constants.py)

Get more information on [Google Spreadsheet API](https://developers.google.com/sheets/api/guides/concepts) & [Sending Email using SMPT](https://www.tutorialspoint.com/python/python_sending_email.htm).

# Here is the data model that this code is written for:

<img width="954" alt="spreadsheet_model_blurred" src="https://user-images.githubusercontent.com/55896033/231042418-665020d8-63a9-4ada-a8b4-754534ad0fcc.png">
