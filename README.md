# Bitbucket CLI Tool

A CLI tool for interacting with the Bitbucket API:

- **auth**: Authenticate via OAuth2 (Authorization Code Flow) and store access token.
- **create-project**: Create new projects in Bitbucket.
- **create-repo**: Create new repositories within a project.
- **add-user**: Add a user to a repository (requires App Password).
- **remove-user**: Remove a user's permission from a repository (requires App Password).
- **configure-branch-permission**: Exempt users from needing a PR on a branch.

## Requirements

- Python 3.10+
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```

## Setup

1. Create a `.env` in the project root with:

   ```
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   REDIRECT_URI=https://localhost:3000/callback
   BITBUCKET_TOKEN=your_oauth_token
   BITBUCKET_USERNAME=your_username
   BITBUCKET_APP_PASSWORD=your_app_password
   ```

2. Run authentication to get or refresh token:

   ```bash
   python main.py auth
   ```

   This will update `BITBUCKET_TOKEN` in `.env`.

3. User management uses App Password because the API only supports this:

   > "The only authentication method for this endpoint is via app passwords."  
   > Source: https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-users-selected-user-id-put

   Permissions can be: `admin`, `write`, `read`.

## Usage

1. **Authenticate** and obtain token:
   ```
   python main.py auth
   ```
2. **Create a project**:
   ```
   python main.py create-project --workspace upwork_challenge --key TEST --name "Project"
   ```
3. **Create a repository**:
   ```
   python main.py create-repo --workspace upwork_challenge --project-key TEST --slug repo --name "Repo"
   ```
4. **Add a user**:
   ```
   python main.py add-user --workspace upwork_challenge --repo repo --user someuser --permission write
   ```
5. **Remove a user**:
   ```
   python main.py remove-user --workspace upwork_challenge --repo repo --user someuser
   ```
6. **Configure branch permission**:
   ```
   python main.py configure-branch-permission --workspace upwork_challenge --repo repo --pattern main --users user
   ```

## Project Structure

```
bitbucket_cli/
├── main.py
├── services/
│   ├── auth.py
│   ├── projects.py
│   ├── repos.py
│   ├── users.py
│   └── branch_permissions.py
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```
