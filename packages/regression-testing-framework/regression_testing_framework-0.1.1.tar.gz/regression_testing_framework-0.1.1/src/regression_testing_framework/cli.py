import click
from regression_testing_framework.celery_tasks import run_test_from_cli
from regression_testing_framework.command_generator import generate_commands

@click.group()
def cli():
    pass

@cli.command()
@click.option('-i', '--input', 'config_path', required=True, type=click.Path(exists=True), help='Path to the YAML configuration file.')
@click.option('-o', '--output', 'output_path', required=False, type=click.Path(), help='Path to save the test run report.')
@click.option('--dry-run', is_flag=True, help='List the commands that will run without executing them.')
def run(config_path, output_path, dry_run):
    if dry_run:
        commands = generate_commands(config_path)
        click.echo(f"Commands to be run ({len(commands)}):")
        for command in commands:
            click.echo(command)
        click.echo(f"Output report will be saved to: {output_path}")
    else:
        run_test_from_cli(config_path, output_path)

if __name__ == '__main__':
    cli()
