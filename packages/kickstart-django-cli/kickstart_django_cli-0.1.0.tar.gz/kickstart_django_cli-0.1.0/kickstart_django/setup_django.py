import re
from rich.console import Console
import sys
import os
import subprocess
from .app_updater import (
    create_app_urls,
    create_home_view,
    update_project_urls,
    create_templates_v2,
)

# Note: We no longer import get_installed_apps_string because we refactored it below.
# from utils import get_installed_apps_string

console = Console()


def get_installed_apps_list(project_type, app_name):
    """
    Return a list of apps that should be added to INSTALLED_APPS,
    based on the project type.
    """
    base_apps = [f"'{app_name}'"]
    match project_type:
        case "Basic Django":
            extra_apps = []
        case "Django + Postgres":
            extra_apps = []
        case "Django + RestFramework":
            extra_apps = ["'rest_framework'"]
        case "Django + Channels":
            # For channels, ensure 'daphne' is at the top and include 'channels'
            extra_apps = ["'daphne'", "'channels'"]
        case _:
            console.print(
                f"[bold red]Unknown project type: {project_type}. Defaulting to Basic Django.[/bold red]"
            )
            extra_apps = []
    return base_apps + extra_apps


def insert_installed_apps(content, additional_apps_list):
    """
    Searches for the INSTALLED_APPS list in the content and injects the additional
    apps at the beginning of the list.
    """
    # Build a string for the additional apps.
    additional_apps_str = ""
    if additional_apps_list:
        additional_apps_str = ", ".join(additional_apps_list) + ", "

    # Regex pattern: capture the part that starts with "INSTALLED_APPS = [", then any content (non-greedy),
    # then the closing bracket.
    pattern = re.compile(r"(INSTALLED_APPS\s*=\s*\[)(.*?)(\])", re.DOTALL)
    match = pattern.search(content)

    if match:
        pre = match.group(1)  # e.g., "INSTALLED_APPS = ["
        existing = match.group(2)  # the existing apps (can be multiline)
        post = match.group(3)  # the closing bracket "]"

        # Insert additional apps at the beginning
        new_installed_apps = pre + additional_apps_str + existing.lstrip() + post

        # Replace the found block with the new block.
        new_content = pattern.sub(new_installed_apps, content, count=1)
        return new_content
    else:
        console.print(
            "[bold red]INSTALLED_APPS not found in settings content.[/bold red]"
        )
        return content


def create_django_project(
    project_folder, project_name, app_name, project_type, db_details, username, password
):
    try:
        # Navigate to the project folder
        os.chdir(project_folder)
        console.print(
            f"[bold green]Creating Django project '{project_name}'...[/bold green]"
        )

        # Create the Django project
        subprocess.run(["django-admin", "startproject", project_name], check=True)
        os.chdir(project_name)

        # Create the Django app
        console.print(
            f"[bold green]Creating the Django app '{app_name}'...[/bold green]"
        )
        subprocess.run([sys.executable, "manage.py", "startapp", app_name], check=True)

        # Create necessary directories
        directories = ["static", "media"]
        if project_type != "Django + RestFramework":
            directories.append("templates")

        console.print(f"Creating necessary directories: {', '.join(directories)}")
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        console.print(f"[bold green]Updating settings...[/bold green]")
        update_settings(project_name, app_name, project_type, db_details)
        console.print(f"[bold green]Running Migrations...[/bold green]")
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
        console.print("[bold green]Creating superuser...[/bold green]")
        subprocess.run(
            [
                sys.executable,
                "manage.py",
                "createsuperuser",
                "--noinput",
                f"--username={username}",
                f"--email={username}@example.com",
            ],
            check=True,
        )

        # Set password separately
        subprocess.run(
            [
                sys.executable,
                "manage.py",
                "shell",
                "-c",
                (
                    f"from django.contrib.auth import get_user_model; "
                    f"User = get_user_model(); "
                    f"user = User.objects.get(username='{username}'); "
                    f"user.set_password('{password}'); "
                    f"user.save()"
                ),
            ],
            check=True,
        )

        console.print(f"[bold green]Adding app views and urls...[/bold green]")
        create_app_urls(app_name, project_type)
        create_home_view(app_name, project_type)
        console.print(f"[bold green]Updating Project urls...[/bold green]")
        update_project_urls(project_name, app_name, project_type)
        create_templates_v2(app_name, project_name, project_type)
        if project_type == "Django + Channels":
            # Create consumers and routing
            create_consumers(app_name)
            create_routing(app_name)

    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error creating Django Project:[/bold red] {e}")


def install_packages(packages):
    """
    Installs the given list of packages into the current virtual environment.

    :param packages: List of package names to install.
    """
    if not isinstance(packages, list):
        console.print("[bold red]Invalid input! Provide a list of packages.[/bold red]")
        return

    # Ensure pip is installed
    try:
        console.print(
            "[bold yellow]Ensuring pip is installed and up-to-date...[/bold yellow]"
        )
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
        )
        console.print("[bold green]pip is installed and updated.[/bold green]")
    except subprocess.CalledProcessError:
        console.print("[bold red]Failed to ensure pip is installed![/bold red]")
        return

    # Install packages
    for package in packages:
        try:
            console.print(f"[bold yellow]Installing {package}...[/bold yellow]")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            console.print(f"[bold green]Successfully installed {package}.[/bold green]")
        except subprocess.CalledProcessError as e:
            console.print(
                f"[bold red]Failed to install {package}. Error: {e}[/bold red]"
            )


def update_settings(project_name, app_name, project_type, db_details=None):
    settings_path = os.path.join(project_name, "settings.py")

    try:
        with open(settings_path, "r") as f:
            content = f.read()

        # Extract and remove SECRET_KEY from the content if present.
        secret_key_match = re.search(r"SECRET_KEY\s*=\s*['\"](.+?)['\"]", content)
        secret_key = secret_key_match.group(1) if secret_key_match else None
        content = re.sub(r"SECRET_KEY\s*=\s*['\"](.+?)['\"]", "", content)

        # Remove existing DATABASES config if db_details provided.
        if db_details:
            content = re.sub(
                r"DATABASES\s*=\s*\{.*?^\}",
                "",
                content,
                flags=re.DOTALL | re.MULTILINE,
            )

        # Prepend the new imports and load .env
        new_content = "import os\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\n"
        new_content += content

        # Add SECRET_KEY from environment
        new_content += "\nSECRET_KEY = os.getenv('SECRET_KEY')\n"

        # Database configuration if provided.
        if db_details:
            new_content += f"""
DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', '{db_details['name']}'),
        'USER': os.getenv('DB_USER', '{db_details['user']}'),
        'PASSWORD': os.getenv('DB_PASSWORD', '{db_details['password']}'),
        'HOST': os.getenv('DB_HOST', '{db_details['host']}'),
        'PORT': os.getenv('DB_PORT', '{db_details['port']}'),
    }}
}}
"""

        # Rest Framework configuration
        if project_type == "Django + RestFramework":
            new_content += """
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
"""

        # Channels configuration and ASGI setup if needed.
        if project_type == "Django + Channels":
            new_content += f"""
# Channels configuration
ASGI_APPLICATION = '{project_name}.asgi.application'
CHANNEL_LAYERS = {{
    "default": {{
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }},
}}
"""
            create_asgi_file(project_name, app_name)

        # At this point, we assume the original settings file has an INSTALLED_APPS block.
        # We inject our additional apps into that block.
        additional_apps_list = get_installed_apps_list(project_type, app_name)
        new_content = insert_installed_apps(new_content, additional_apps_list)

        # Append the remaining common settings (static, media, templates)
        new_content += (
            "\nMEDIA_URL = '/media/'\n"
            "MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n\n"
            "STATIC_URL = '/static/'\n"
            "STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]\n"
            "STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n\n"
            "TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'templates'))\n"
        )

        # Write out the modified settings file.
        with open(settings_path, "w") as f:
            f.write(new_content)

        # Create .env file with proper secret key and db details.
        create_env_file(secret_key, db_details)

    except Exception as e:
        console.print(f"[bold red]Error updating settings:[/bold red] {e}")


def create_asgi_file(project_name, app_name):
    asgi_content = f"""import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import {app_name}.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{project_name}.settings')

application = ProtocolTypeRouter({{
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            {app_name}.routing.websocket_urlpatterns
        )
    ),
}})
"""
    with open(os.path.join(project_name, "asgi.py"), "w") as f:
        f.write(asgi_content)


def create_consumers(app_name):
    consumers_content = """
import json
import math
from channels.generic.websocket import WebsocketConsumer

class Calculator(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        expression = text_data_json['expression']
        try:
            # Evaluate only safe arithmetic expressions
            result = eval(expression, {"__builtins__": None}, {"math": math})
        except Exception as e:
            result = "Invalid Expression"
        self.send(text_data=json.dumps({
            'result': result
        }))
"""
    with open(os.path.join(app_name, "consumers.py"), "w") as f:
        f.write(consumers_content)


def create_routing(app_name):
    routing_content = """from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/livec/$', consumers.Calculator.as_asgi()),
]
"""
    with open(os.path.join(app_name, "routing.py"), "w") as f:
        f.write(routing_content)


def create_env_file(secret_key, db_details=None):
    with open(".env", "w") as f:
        f.write(f"SECRET_KEY={secret_key}\n")
        if db_details:
            f.write(f"DB_NAME={db_details['name']}\n")
            f.write(f"DB_USER={db_details['user']}\n")
            f.write(f"DB_PASSWORD={db_details['password']}\n")
            f.write(f"DB_HOST={db_details['host']}\n")
            f.write(f"DB_PORT={db_details['port']}\n")


def setting_up(
    project_name, app_name, requirements, project_type, db_details, username, password
):
    try:
        # Install requirements
        install_packages(requirements)

        # Generate requirements.txt
        with open("requirements.txt", "w") as f:
            subprocess.run(
                [sys.executable, "-m", "pip", "freeze"], stdout=f, check=True
            )

        # Create project
        create_django_project(
            os.getcwd(),
            project_name,
            app_name,
            project_type,
            db_details,
            username,
            password,
        )

    except Exception as e:
        console.print(f"[bold red]Setup error:[/bold red] {e}")
