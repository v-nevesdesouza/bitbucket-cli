import typer
from services.projects import create_project

app = typer.Typer()

@app.command()
def new_project(workspace: str, key: str, name: str):
    result = create_project(workspace, key, name)
    typer.echo(result)

if __name__ == "__main__":
    app()
