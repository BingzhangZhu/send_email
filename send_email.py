import smtplib, mimetypes, os
from email.message import EmailMessage
from email.utils import COMMASPACE

ACCOUNT_INFO = {'username':'email', 'password':'pass'} # TODO:

def send_email(recipients, subject, body, filename=None, account_info=ACCOUNT_INFO):
    
    # creates an instance of EmailMessage
    message = EmailMessage()
    # set params of the email 
    message['From'] = account_info['username']
    message['To'] = COMMASPACE.join(recipients)
    message['Subject'] = subject
    message.set_content(body)

    # get the MIME type and subtype of the attachment 
    mime_type, _ = mimetypes.guess_type(filename)
    mime_type, mime_subtype = mime_type.split('/')
    # store the attachment to the message if the file exists
    if filename:
        if not os.path.isfile(filename):
            raise ValueError(f"File does not exist: {filename}")
        with open('attachment.csv', 'rb') as file:
            message.add_attachment(file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename='attachment.csv')

    # TODO: delete this 
    print(message)

    # creates SMTP_SSL session to connect securely to the remote server.
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    # Authentication
    mail_server.login(account_info['username'], account_info['password'])
    # sending the mail
    mail_server.send_message(message)
    # terminating the session
    mail_server.quit()

if __name__=="__main__":

    # create the attachment
    # import pandas as pd
    # data = {'a': [1, 3], 'b': [2, 4]}
    # df = pd.DataFrame(data = data)
    # df.to_csv("attachment.csv")
    recipients = ["bingzhangzhu@outlook.com"]
    subject = ""
    body = """Hello
    I am learning to send emails using Python!!!"""
    # ACCOUNT_INFO = None # TODO
    send_email(recipients, subject, body, "attachment.csv")
    # TODO: env + readme.md