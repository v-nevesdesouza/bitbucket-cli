import typer
from services.auth import get_token
from services.projects import create_project_cli
from services.repos import create_repo_cli
from services.users import add_user_cli, remove_user_cli
from services.branch_permissions import configure_branch_permission_cli

app = typer.Typer(help="Bitbucket CLI Tool")

@app.command()
def auth():
    """
    Authenticate with Bitbucket OAuth2 and save access token to .env
    """
    get_token()

@app.command("create-project")
def create_project(
    workspace: str = typer.Option(..., "--workspace", "-w", help="Bitbucket workspace ID"),
    key: str = typer.Option(..., "--key", "-k", help="Project key"),
    name: str = typer.Option(..., "--name", "-n", help="Project name")
):
    """
    Create a new Bitbucket project in the specified workspace.
    """
    create_project_cli(workspace, key, name)

@app.command("create-repo")
def create_repo(
    workspace: str = typer.Option(..., "--workspace", "-w", help="Bitbucket workspace ID"),
    project_key: str = typer.Option(..., "--project-key", "-p", help="Existing project key"),
    slug: str = typer.Option(..., "--slug", "-s", help="Repository slug"),
    name: str = typer.Option(..., "--name", "-n", help="Repository name")
):
    """
    Create a new repository under a specified project.
    """
    create_repo_cli(workspace, project_key, slug, name)

@app.command("add-user")
def add_user(
    workspace: str = typer.Option(..., "--workspace", "-w", help="Bitbucket workspace ID"),
    repo_slug: str = typer.Option(..., "--repo", "-r", help="Repository slug"),
    username: str = typer.Option(..., "--user", "-u", help="Username to add"),
    permission: str = typer.Option("write", "--permission", "-p", help="Permission level (read, write, admin)")
):
    """
    Add a user to a repository with specified permission.
    """
    add_user_cli(workspace, repo_slug, username, permission)

@app.command("remove-user")
def remove_user(
    workspace: str = typer.Option(..., "--workspace", "-w", help="Bitbucket workspace ID"),
    repo_slug: str = typer.Option(..., "--repo", "-r", help="Repository slug"),
    username: str = typer.Option(..., "--user", "-u", help="Username to remove")
):
    """
    Remove a user's permission from a repository.
    """
    remove_user_cli(workspace, repo_slug, username)

@app.command("configure-branch-permission")
def configure_branch_permission(
    workspace: str = typer.Option(..., "--workspace", "-w", help="Bitbucket workspace ID"),
    repo_slug: str = typer.Option(..., "--repo", "-r", help="Repository slug"),
    pattern: str = typer.Option("main", "--pattern", "-p", help="Branch name or glob pattern"),
    users: str = typer.Option(..., "--users", "-u", help="Comma-separated list of usernames to exempt")
):
    """
    Configure branch permission to allow specified users direct push without PR.
    """
    user_list = [u.strip() for u in users.split(",")]
    configure_branch_permission_cli(workspace, repo_slug, pattern, user_list)

if __name__ == "__main__":
    app()
