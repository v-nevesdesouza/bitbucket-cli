import requests
from services.auth import HEADERS

def create_project(workspace: str, key: str, name: str):
    """
    Creates a new Bitbucket project within a given workspace.
    """
    url = f"https://api.bitbucket.org/2.0/workspaces/{workspace}/projects/"
    payload = { "key": key, "name": name }
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()
