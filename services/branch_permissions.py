import os
import requests
from dotenv import load_dotenv

load_dotenv()

def configure_branch_permission_cli(workspace: str, repo_slug: str, pattern: str, users: list):
    token = os.getenv("BITBUCKET_TOKEN")
    if not token:
        print("❌ BITBUCKET_TOKEN is not set. Please run 'auth' first.")
        return
    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/branch-restrictions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    user_objs = [{"type": "user", "username": u} for u in users]
    payload = {
        "kind": "push",
        "pattern": pattern,
        "branch_match_kind": "glob",
        "users": user_objs
    }
    resp = requests.post(url, json=payload, headers=headers)
    if resp.status_code == 201:
        print("✅ Branch permission configured successfully:")
        print(resp.json())
    else:
        print(f"❌ Failed to configure branch permission: HTTP {resp.status_code}")
        print(resp.text)
