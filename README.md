# okta-auth-token-checker

You can use this to check if an Okta auth token is valid or not. I made this to debug an annoying issue and it might be useful for someone out there :)

# Setup

Create a `.env` with the following content:

```env
OKTA_ISSUER=https://{{your okta domain}}.okta.com/oauth2/default
OKTA_CLIENT_ID=your okta client id
OKTA_CLIENT_SECRET=your okta client secret
```

Create a `venv` and install from `requirements.txt`

```bash
python3 -m venv venv
source venv/bin/Activate 
pip install -r requirements.txt
```

# How to Use

Run `main.py` and pass in your accessToken:

```bash
python3 main.py eyJraWQiOiJLR1hjUTVpZEkyaE...
```

If the token is valid you will see your accessToken data

If it is invalid (or expired) you will see a message saying the token is invalid

