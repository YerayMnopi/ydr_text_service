import typer

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


from src.infrastructure.data.mappers import start_mappers
from src.settings import get_settings


app = typer.Typer()


@app.command()
def create_db():
    from .init_db import InitDBCommand
    typer.echo(f"Creating DB")
    InitDBCommand().handle()
    typer.echo(f"DB created")

if __name__ == "__main__":
    app()