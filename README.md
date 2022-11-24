# Send email with attachment through python script.

## Usage

1. Install the required library using `pip install -r requirement.txt`
2. Edit the two files: `config/gmail_account_info.json` and `config/email_info.json`
3. Run the script using `sh run.sh`

## Structure:
```
├── attachment.csv
├── config
│   ├── email_info.json
│   └── gmail_account_info.json
├── out.log
├── README.md
├── requirement.txt
├── run.sh
└── send_email.py
```

## Reference:
1. https://levelup.gitconnected.com/send-email-using-python-30fc1f203505
2. https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp 