import json_manager
import click

@click.group()
def cli():
    pass

@cli.command()
def user():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

if __name__ == '__main__':
    cli()

