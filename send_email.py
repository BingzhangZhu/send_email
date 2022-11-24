import os
import json
import argparse
import smtplib
import mimetypes
from email.message import EmailMessage
from email.utils import COMMASPACE

def get_config(file_name):
    """_summary_

    Args:
        file_name (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(file_name, 'r') as config_json:
        config_data = json.load(config_json)
    return config_data

def send_email(account_info, recipients, subject, body, filename=None):
    """
    Args:
        account_info (_type_): _description_
        recipients (_type_): _description_
        subject (_type_): _description_
        body (_type_): _description_
        filename (_type_, optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_
    """
    
    # creates an instance of EmailMessage
    message = EmailMessage()
    # set params of the email 
    message['From'] = account_info['username']
    message['To'] = COMMASPACE.join(recipients)
    message['Subject'] = subject
    message.set_content(body)

    # store the attachment to the message if the file exists
    if filename:
        if not os.path.isfile(filename):
            raise ValueError(f"File does not exist: {filename}")
        # get the MIME type and subtype of the attachment 
        mime_type, _ = mimetypes.guess_type(filename)
        mime_type, mime_subtype = mime_type.split('/')
        with open('attachment.csv', 'rb') as file:
            message.add_attachment(file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename='attachment.csv')

    # print message in log
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

    parser = argparse.ArgumentParser(description='Send email.')
    parser.add_argument('account_info_path', type=str, 
                        help='path to the email account info config')
    parser.add_argument('email_info_path', type=str, 
                        help='path to the email info config')
    args = parser.parse_args()
    
    gmail_account_info = get_config(args.account_info_path)
    email_info = get_config(args.email_info_path)
    
    send_email(gmail_account_info, email_info["recipients"], email_info["subject"], email_info["body"], email_info.get("attachment", None))