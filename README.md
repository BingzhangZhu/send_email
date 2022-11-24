# Send email with attachment through python script.

## Usage

1. Edit the two files: `config/sender_account.json` and `config/email_info.json`. (If you are using Gmail as the sender account, set the App Passwords according to the 2nd reference. The App Password is a 16-character code and you should use it as the password here)
2. Run the script using `sh run.sh`

## Structure:
```
├── attachment.csv
├── config
│   ├── email_info.json
│   └── sender_account.json
├── README.md
├── run.sh
└── send_email.py
```

## Reference:
1. https://levelup.gitconnected.com/send-email-using-python-30fc1f203505
2. https://support.google.com/accounts/answer/185833?hl=en