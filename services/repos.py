import os
import requests
from dotenv import load_dotenv

load_dotenv()

def create_repo_cli(workspace: str, project_key: str, slug: str, name: str):
    token = os.getenv("BITBUCKET_TOKEN")
    if not token:
        print("❌ BITBUCKET_TOKEN is not set. Please run 'auth' first.")
        return
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{slug}"
    payload = {
        "scm": "git",
        "is_private": True,
        "project": {"key": project_key},
        "name": name
    }
    resp = requests.post(url, json=payload, headers=headers)
    if resp.status_code in (200, 201):
        print("✅ Repository created successfully:")
        print(resp.json())
    else:
        print(f"❌ Failed to create repository: HTTP {resp.status_code}")
        print(resp.text)
