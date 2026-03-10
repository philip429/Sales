# clients/commands.py
import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the client's life cycle."""
    pass  # placeholder para evitar error

@clients.command()
@click.option('-n','--name', type=str, prompt=True, help="The client's name.")
@click.option('-c','--company', type=str, prompt=True, help="The client's company.")
@click.option('-e','--email', type=str, prompt=True, help="The client's email.")
@click.option('-p','--position', type=str, prompt=True, help="The client's position.")
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates New Client"""
    client = Client(name,company,email,position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command("list")  # evitar colisión con palabra reservada list
@click.pass_context
def list_cmd(ctx):
    """List all clients."""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_client()

    click.echo('  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  ')
    click.echo('*' *100)
    
    for client in client_list:
        click.echo(f"  {client['uid']}  |  {client['name']}  | {client['company']}  |  {client['email']}  |  {client['position']}  ")

@clients.command()
@click.argument('client_uid',type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client = [client for client in client_service.list_client() if client['uid'] == client_uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')

def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)
    
    return client

@clients.command()
@click.argument('client_uid',type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Delete a client."""
    client_service = ClientService(ctx.obj['clients_table'])
    
    client = [client for client in client_service.list_client() if client['uid'] == client_uid]

    if client:
        client_service.delete_client(Client(**client[0]))
        click.echo('Client Delete')
    else:
        click.echo('Client not found')


# alias para registrar todo el grupo desde PV.py
all = clients

