import webbrowser
import urllib.parse
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://localhost:3000/callback")
SCOPES = "project:write repository:admin"

if not CLIENT_ID or not CLIENT_SECRET:
    raise EnvironmentError("CLIENT_ID and CLIENT_SECRET must be set in .env")

def get_token():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES
    }
    auth_url = "https://bitbucket.org/site/oauth2/authorize?" + urllib.parse.urlencode(params)
    print("🔗 Authorization URL:")
    print(auth_url)
    webbrowser.open(auth_url)

    callback_url = input("\nPaste the full callback URL here: ").strip()
    parsed = urllib.parse.urlparse(callback_url)
    code = urllib.parse.parse_qs(parsed.query).get("code", [None])[0]
    if not code:
        print("❌ Authorization code not found in URL.")
        return

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    response = requests.post(
        "https://bitbucket.org/site/oauth2/access_token",
        data=data,
        auth=(CLIENT_ID, CLIENT_SECRET)
    )
    if response.status_code != 200:
        print(f"❌ Failed to exchange code: HTTP {response.status_code}")
        print(response.text)
        return

    token_data = response.json()
    access_token = token_data.get("access_token")
    if not access_token:
        print("❌ No access token received.")
        return

    env_path = ".env"
    lines = []
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            lines = f.readlines()
    key_found = False
    with open(env_path, "w") as f:
        for line in lines:
            if line.startswith("BITBUCKET_TOKEN="):
                f.write(f"BITBUCKET_TOKEN={access_token}\n")
                key_found = True
            else:
                f.write(line)
        if not key_found:
            f.write(f"BITBUCKET_TOKEN={access_token}\n")
    print("✅ Access token obtained and saved to .env")
