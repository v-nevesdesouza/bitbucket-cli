import os
import requests
from dotenv import load_dotenv

load_dotenv()

def create_project_cli(workspace: str, key: str, name: str):
    token = os.getenv("BITBUCKET_TOKEN")
    if not token:
        print("❌ BITBUCKET_TOKEN is not set. Please run 'auth' first.")
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    url = f"https://api.bitbucket.org/2.0/workspaces/{workspace}/projects/"
    payload = {"key": key, "name": name}
    resp = requests.post(url, json=payload, headers=headers)
    if resp.status_code == 201:
        print("✅ Project created successfully:")
        print(resp.json())
    else:
        print(f"❌ Failed to create project: HTTP {resp.status_code}")
        print(resp.text)
