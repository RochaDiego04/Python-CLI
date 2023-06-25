import json_manager
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help="Name of the user")
@click.option('--lastname', required=True, help="Name of the user")
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail('The name and lastname are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'lastname': lastname
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} created successfully with id {new_id}")


@cli.command()
def user():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")

if __name__ == '__main__':
    cli()

