# dc-texter

> Send an SMS text alert using Python and Gmail

## Requirements

- Python 3.11+ (required for reading toml files)
- A configured Gmail Account (see below)

---

## Step 1. Install this Module

Run

```
pip install dc-texter
```

Or: add `dc-texter` to requirements.txt and install. 

---

## Step 2. Configure Application Settings

### Local Development
For local development, we can configure our settings with a file.
First, add .env.toml to .gitignore to keep it from being published.
Then, create a .env.toml file in your project directory with the following.
```
outgoing_email_host = "smtp.gmail.com"
outgoing_email_port = 587
outgoing_email_address = "youremail@gmail.com"
outgoing_email_password = "aaaabbbbccccdddd"
sms_address_for_texts = "1112224444@msg.fi.google.com"
```

### GitHub Action Deployments
In a deployment environment like GitHub Actions, the .env.toml file won't be available. Instead, you'll need to set the configuration variables as environment variables.

First, add the following secrets to your GitHub repository:

1. Navigate to your repository on GitHub.
2. Click on Settings > Secrets and variables > Actions.
3. Click on New repository secret and add the following secrets:
    - OUTGOING_EMAIL_HOST: Set this to "smtp.gmail.com".
    - OUTGOING_EMAIL_PORT: Set this to 587.
    - OUTGOING_EMAIL_ADDRESS: Set this to your gmail address.
    - OUTGOING_EMAIL_PASSWORD: Set this to your application password.
    - SMS_ADDRESS_FOR_TEXTS: Set this to your phonenumber@your.provider.gateway

Next, reference these secrets in your GitHub Actions workflow. 
For an example, see [this deploy.yml](https://github.com/denisecase/kafka-producer-earthquake/blob/main/.github/workflows/deploy.yml).

---

## Step 3. Configure Gmail 

Enable IMAP

 - Open Gmail. Click Settings or ⚙️ in the top-right.
 - Click "See all settings". Navigate to "Forwarding and POP/IMAP".
 - Under "IMAP access", select "Enable IMAP" and save changes.

Generate an App Password

- If you have 2-Step Verification enabled, create an app password for "dc-mailer".
- Copy the 16-character password displayed.
- Paste the 16-char as your password in .env.toml file. Remove spaces.
- For detailed instructions, refer to [Google's support page](https://support.google.com/accounts/answer/185833?hl=en).

---


## Step 4. Import and Use in a Python Script

Once installed and your .env.toml file is ready, you can use it in your code. 

```python
from dc_texter import send_text

message = "Testing text alerts from Python."

try:
    send_text(body=message)
    print(f"SUCCESS. Text sent: {message}")
except RuntimeError as e:
    print(f"ERROR:  Sending failed: {e}")
```
