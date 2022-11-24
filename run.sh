#!/usr/bin/env bash

account_info="config/sender_account.json"
email_info="config/email_info.json"

python3 send_email.py $account_info $email_info >> out.log