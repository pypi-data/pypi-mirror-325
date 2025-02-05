import os
import sys
import tempfile
import webbrowser

import click
import pkg_resources

from preswald.deploy import deploy as deploy_app
from preswald.deploy import stop as stop_app
from preswald.main import start_server
from preswald.utils import configure_logging, read_template

# Create a temporary directory for IPC
TEMP_DIR = os.path.join(tempfile.gettempdir(), "preswald")
os.makedirs(TEMP_DIR, exist_ok=True)


@click.group()
@click.version_option()
def cli():
    """
    Preswald CLI - A lightweight framework for interactive data apps.
    """
    pass


@cli.command()
@click.argument("name", default="preswald_project")
def init(name):
    """
    Initialize a new Preswald project.

    This creates a directory with boilerplate files like `hello.py` and `preswald.toml`.
    """
    try:
        os.makedirs(name, exist_ok=True)
        os.makedirs(os.path.join(name, "images"), exist_ok=True)

        # Copy default branding files from package resources
        import shutil

        default_static_dir = pkg_resources.resource_filename("preswald", "static")
        default_favicon = os.path.join(default_static_dir, "favicon.ico")
        default_logo = os.path.join(default_static_dir, "logo.png")

        shutil.copy2(default_favicon, os.path.join(name, "images", "favicon.ico"))
        shutil.copy2(default_logo, os.path.join(name, "images", "logo.png"))

        file_templates = {
            "hello.py": "hello.py",
            "preswald.toml": "preswald.toml",
            "secrets.toml": "secrets.toml",
            ".gitignore": "gitignore",
            "README.md": "readme.md",
            "pyproject.toml": "pyproject.toml",
        }

        for file_name, template_name in file_templates.items():
            content = read_template(template_name)
            with open(os.path.join(name, file_name), "w") as f:
                f.write(content)

        click.echo(f"Initialized a new Preswald project in '{name}/' 🎉!")
    except Exception as e:
        click.echo(f"Error initializing project: {e} ❌")


@cli.command()
@click.argument("script", default="hello.py")
@click.option("--port", default=8501, help="Port to run the server on.")
@click.option(
    "--log-level",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
    default=None,
    help="Set the logging level (overrides config file)",
)
def run(script, port, log_level):
    """
    Run a Preswald app.

    By default, it runs the `hello.py` script on localhost:8501.
    """
    if not os.path.exists(script):
        click.echo(f"Error: Script '{script}' not found. ❌")
        return

    config_path = os.path.join(os.path.dirname(script), "preswald.toml")
    log_level = configure_logging(config_path=config_path, level=log_level)

    url = f"http://localhost:{port}"
    click.echo(f"Running '{script}' on {url} with log level {log_level}  🎉!")

    # ipc_file = os.path.join(TEMP_DIR, f"preswald_connections_{os.getpid()}.json")
    # os.environ["PRESWALD_IPC_FILE"] = ipc_file

    # celery_cmd = [
    #     "celery",
    #     "-A", "preswald.celery_app",
    #     "worker",
    #     "--loglevel", log_level.lower(),
    #     "--concurrency", "1",
    #     "--pool", "solo",
    #     "--without-heartbeat",
    #     "--without-mingle",
    #     "--without-gossip"
    # ]

    try:
        # click.echo("Starting Celery worker...")
        # celery_process = subprocess.Popen(
        #     celery_cmd,
        #     env=dict(
        #         os.environ,
        #         SCRIPT_PATH=os.path.abspath(script),
        #         PYTHONPATH=os.getcwd(),
        #         PYTHONUNBUFFERED="1"
        #     )
        # )

        # # Wait for Celery to start
        # import time
        # time.sleep(2)

        # if celery_process.poll() is not None:
        #     out, err = celery_process.communicate()
        #     click.echo(f"Error starting Celery worker: {err}")
        #     return

        webbrowser.open(url)

        # try:
        start_server(script=script, port=port)
        # finally:
        #     click.echo("Shutting down Celery worker...")
        #     celery_process.terminate()
        #     celery_process.wait(timeout=5)

        #     try:
        #         if os.path.exists(ipc_file):
        #             os.remove(ipc_file)
        #     except Exception as e:
        #         click.echo(f"Error removing IPC file: {e}")

    except Exception as e:
        click.echo(f"Error: {e}")
        # if 'celery_process' in locals():
        #     celery_process.terminate()
        #     celery_process.wait(timeout=5)


@cli.command()
@click.argument("script", default="app.py")
@click.option(
    "--target",
    type=click.Choice(["local", "gcp", "aws", "structured"], case_sensitive=False),
    default="local",
    help="Target platform for deployment.",
)
@click.option("--port", default=8501, help="Port for deployment.")
@click.option(
    "--log-level",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
    default=None,
    help="Set the logging level (overrides config file)",
)
def deploy(script, target, port, log_level):
    """
    Deploy your Preswald app.

    This allows you to share the app within your local network or deploy to production.
    """
    try:
        if target == "aws":
            click.echo(
                f"\nWe're working on supporting AWS soon! Please enjoy some ☕ and 🍌 in the meantime"
            )
            return

        if not os.path.exists(script):
            click.echo(f"Error: Script '{script}' not found. ❌")
            return

        config_path = os.path.join(os.path.dirname(script), "preswald.toml")
        log_level = configure_logging(config_path=config_path, level=log_level)

        if target == "structured":
            click.echo("Starting production deployment... 🚀")
            try:
                for status_update in deploy_app(script, target, port=port):
                    status = status_update.get('status', '')
                    message = status_update.get('message', '')
                    timestamp = status_update.get('timestamp', '')
                    
                    if status == 'error':
                        click.echo(click.style(f"❌ {message}", fg='red'))
                    elif status == 'success':
                        click.echo(click.style(f"✅ {message}", fg='green'))
                    else:
                        click.echo(f"ℹ️  {message}")
                        
            except Exception as e:
                click.echo(click.style(f"Deployment failed: {str(e)} ❌", fg='red'))
                return
        else:
            url = deploy_app(script, target, port=port)
            
            ## Deployment Success Message
            success_message = """
            
            ===========================================================\n
            🎉 Deployment successful! ✅

            🌐 Your app is live and running at:
            {url}

            💡 Next Steps:
                - Open the URL above in your browser to view your app

            🚀 Deployment Summary:
                - App: {script}
                - Environment: {target}
                - Port: {port}
            """.format(
                script=script, url=url, target=target, port=port
            )

            click.echo(click.style(success_message, fg="green"))

    except Exception as e:
        click.echo(f"Error deploying app: {e} ❌")


@cli.command()
@click.argument("script", default="app.py")
def stop(script):
    """
    Stop the currently running deployment.

    This command must be run from the same directory as your Preswald app.
    """
    try:
        if not os.path.exists(script):
            click.echo(f"Error: Script '{script}' not found. ❌")
            return
        stop_app(script)
        click.echo("Deployment stopped successfully. 🛑 ")
    except Exception as e:
        click.echo(f"Error stopping deployment: {e} ❌")
        sys.exit(1)


if __name__ == "__main__":
    cli()
