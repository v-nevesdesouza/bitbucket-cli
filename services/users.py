import os
import requests
from dotenv import load_dotenv

load_dotenv()

def add_user_cli(workspace: str, repo_slug: str, username: str, permission: str):
    app_user = os.getenv("BITBUCKET_USERNAME")
    app_pass = os.getenv("BITBUCKET_APP_PASSWORD")
    if not app_user or not app_pass:
        print("❌ BITBUCKET_USERNAME or BITBUCKET_APP_PASSWORD not set. Please set app credentials.")
        return
    headers = {"Content-Type": "application/json"}
    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{username}"
    payload = {"permission": permission}
    resp = requests.put(url, json=payload, headers=headers, auth=(app_user, app_pass))
    if resp.status_code in (200, 201):
        print("✅ User added with permission:")
        print(resp.json())
    else:
        print(f"❌ Failed to add user: HTTP {resp.status_code}")
        print(resp.text)
def remove_user_cli(workspace: str, repo_slug: str, username: str):
    app_user = os.getenv("BITBUCKET_USERNAME")
    app_pass = os.getenv("BITBUCKET_APP_PASSWORD")
    if not app_user or not app_pass:
        print("❌ BITBUCKET_USERNAME or BITBUCKET_APP_PASSWORD not set. Please set app credentials.")
        return
    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/permissions-config/users/{username}"
    resp = requests.delete(url, auth=(app_user, app_pass))
    if resp.status_code == 204:
        print("✅ User removed successfully.")
    else:
        print(f"❌ Failed to remove user: HTTP {resp.status_code}")
    print(resp.text)
