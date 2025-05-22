import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Read token from environment variable
TOKEN = os.getenv("BITBUCKET_TOKEN")

if not TOKEN:
    raise EnvironmentError("BITBUCKET_TOKEN environment variable not set")

# Authorization headers for Bitbucket API
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
