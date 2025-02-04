import click
from multi_swarm.utils.project_setup import init_project

@click.group()
def cli():
    """Multi-Swarm CLI tools."""
    pass

@cli.command()
@click.argument('project_name', required=False)
def init(project_name: str = None):
    """Initialize a new Multi-Swarm project."""
    init_project(project_name)

if __name__ == '__main__':
    cli() 