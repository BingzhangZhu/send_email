import os
import json
import argparse
import smtplib
import mimetypes
from email.message import EmailMessage
from email.utils import COMMASPACE

def get_config(file_name):
    
    with open(file_name, 'r') as config_json:
        config_data = json.load(config_json)
    return config_data

def send_email(account_info, recipients, cc, subject, body, file_path=None):
    """
    Args:
        account_info (dict): email account info including username and password
        recipients (list): a list of recipients
        cc (list): a list of carbon copy
        subject (str): the subject of the email
        body (str): the body of the email
        file_path (str, optional): the path to the attachment. Defaults to None.

    Raises:
        ValueError: Invalid file path
    """
    
    # creates an instance of EmailMessage
    message = EmailMessage()
    # set params of the email 
    message['From'] = account_info['username']
    message['To'] = COMMASPACE.join(recipients)
    message['CC'] = cc
    message['Subject'] = subject
    message.set_content(body)

    # store the attachment to the message if the file exists
    if file_path:
        if not os.path.isfile(file_path):
            raise ValueError(f"File does not exist: {file_path}")
        # get the MIME type and subtype of the attachment 
        mime_type, _ = mimetypes.guess_type(file_path)
        mime_type, mime_subtype = mime_type.split('/')
        with open(file_path, 'rb') as file:
            message.add_attachment(file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=os.path.split(file_path)[-1])

    # print message in log
    print(message)

    # creates SMTP_SSL session to connect securely to the remote server.
    mail_server = smtplib.SMTP_SSL(account_info['smtp_server'])
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

    parser = argparse.ArgumentParser(description='send email')
    parser.add_argument('account_info_path', type=str, 
                        help='path to the email account info config')
    parser.add_argument('email_info_path', type=str, 
                        help='path to the email info config')
    args = parser.parse_args()
    
    sender_account_info = get_config(args.account_info_path)
    email_info = get_config(args.email_info_path)
    
    send_email(sender_account_info, email_info["recipients"], email_info["cc"], email_info["subject"], email_info["body"], email_info.get("attachment", None))