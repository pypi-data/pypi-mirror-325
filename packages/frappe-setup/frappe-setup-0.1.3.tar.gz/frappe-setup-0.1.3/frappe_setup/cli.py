import click
import os
import subprocess
import shutil
from pathlib import Path
import pkg_resources

@click.group()
def main():
    """Frappe Framework Setup Tool"""
    pass

@main.command()
@click.option('--path', default='.', help='Installation path')
def install(path):
    """Install Frappe Framework with Docker setup"""
    click.echo("Starting Frappe Framework installation...")
    
    # Create installation directory
    install_path = Path(path).absolute()
    os.makedirs(install_path, exist_ok=True)
    os.chdir(install_path)

    # Clone frappe_docker repository
    if not os.path.exists('frappe_docker'):
        subprocess.run(['git', 'clone', 'https://github.com/frappe/frappe_docker.git'], check=True)

    os.chdir('frappe_docker')

    # Copy development container configurations
    shutil.copytree('devcontainer-example', '.devcontainer', dirs_exist_ok=True)
    shutil.copytree('development/vscode-example', 'development/.vscode', dirs_exist_ok=True)

    # Install VS Code extension
    subprocess.run(['code', '--install-extension', 'ms-vscode-remote.remote-containers'], check=True)

    click.echo("Installation completed!")
    click.echo("\nTo start development:")
    click.echo("1. cd " + str(install_path) + "/frappe_docker")
    click.echo("2. code .")
    click.echo("3. When VS Code opens, click 'Reopen in Container' when prompted")

@main.command()
@click.option('--path', default='.', help='Installation path')
def setup_bench(path):
    """Setup Frappe Bench inside the container"""
    install_path = Path(path).absolute() / 'frappe_docker'
    os.chdir(install_path)

    # Rebuild container with devcontainer CLI
    subprocess.run([
        'devcontainer', 'up', '--workspace-folder', '.'
    ], check=True)

    # Commands to run inside the container
    commands = [
        ['bench', 'init', '--skip-redis-config-generation', '--frappe-branch', 'version-15', 'frappe-bench'],
        ['bench', 'set-config', '-g', 'db_host', 'mariadb'],
        ['bench', 'set-config', '-g', 'redis_cache', 'redis://redis-cache:6379'],
        ['bench', 'set-config', '-g', 'redis_queue', 'redis://redis-queue:6379'],
        ['bench', 'set-config', '-g', 'redis_socketio', 'redis://redis-queue:6379'],
        ['sed', '-i', '/redis/d', './Procfile'],
        ['bench', 'new-site', '--mariadb-root-password', '123', '--admin-password', 'admin', '--no-mariadb-socket', 'development.localhost'],
        ['bench', 'config', 'set-common-config', '-c', 'root_login', 'postgres'],
        ['bench', 'config', 'set-common-config', '-c', 'root_password', '"123"'],
        ['bench', '--site', 'development.localhost', 'set-config', 'developer_mode', '1'],
        ['bench', '--site', 'development.localhost', 'clear-cache'],
        ['bench', 'get-app', '--branch', 'version-15', '--resolve-deps', 'erpnext'],
        ['bench', '--site', 'development.localhost', 'install-app', 'erpnext']
    ]

    # Execute commands in container environment
    for cmd in commands:
        subprocess.run([
            'devcontainer', 'exec', 
            '--workspace-folder', '.',
            'sh', '-c', ' '.join(cmd)
        ], check=True)
    
    click.echo("\nSetup completed! Access your site at:")
    click.echo("http://development.localhost:8000")
    click.echo("Username: Administrator")
    click.echo("Password: admin")

@main.command()
@click.option('--path', default='.', help='Installation path')
def uninstall(path):
    """Uninstall Frappe Framework and clean up Docker setup"""
    click.echo("Starting Frappe Framework uninstallation...")
    
    install_path = Path(path).absolute()
    
    if click.confirm('This will remove all Frappe related files and Docker containers. Continue?'):
        try:
            # Stop and remove Docker containers
            if os.path.exists(os.path.join(install_path, 'frappe_docker')):
                os.chdir(os.path.join(install_path, 'frappe_docker'))
                subprocess.run(['docker-compose', 'down', '-v'], check=True)

            # Remove the frappe_docker directory
            if os.path.exists(os.path.join(install_path, 'frappe_docker')):
                shutil.rmtree(os.path.join(install_path, 'frappe_docker'))

            click.echo("Frappe Framework files and Docker containers have been removed.")
            click.echo("\nTo completely remove the frappe-setup package, run:")
            click.echo("pip uninstall frappe-setup")
            
        except Exception as e:
            click.echo(f"Error during uninstallation: {str(e)}")
    else:
        click.echo("Uninstallation cancelled.")

if __name__ == '__main__':
    main() 