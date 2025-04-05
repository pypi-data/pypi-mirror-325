from rich.console import Console
from rich.panel import Panel
import questionary
from .utils import validate__name, password_validator, create_requirements
from .setup_django import setting_up
from questionary import Style

custom_style = Style(
    [
        ("qmark", "fg:#00FF00 bold"),
        ("question", "fg:#00FFFF bold"),
        ("answer", "fg:#FFAA00 bold"),
        ("pointer", "fg:#FF0000 bold"),
        ("highlighted", "fg:#FFFF00 bold"),
        ("selected", "fg:#00FF00 bold"),
        ("instruction", "fg:#AAAAAA italic"),
    ]
)

console = Console()


def user_prompt():
    console.print(
        Panel.fit(
            "[bold cyan]🚀 Django Kickstart 🚀[/bold cyan]\n"
            "[italic white]Quickly set up your Django project with ease![/italic white]",
            style="bold green",
            border_style="bright_yellow",
        )
    )
    project_name = (
        questionary.text(
            "What is your project name? (default: myproject)",
            style=custom_style,
            validate=validate__name,
        ).ask()
        or "myproject"
    )

    app_name = (
        questionary.text(
            "Enter the name of your Django app (default: myapp)",
            validate=validate__name,
            style=custom_style,
        ).ask()
        or "myapp"
    )

    username = (
        questionary.text(
            "Enter the superuser username (default: admin)",
            style=custom_style,
        ).ask()
        or "admin"
    )

    password = (
        questionary.password(
            "Enter the superuser password (default: admin123)",
            style=custom_style,
            validate=password_validator,
        ).ask()
        or "admin123"
    )

    project_type = questionary.select(
        "Select your project type",
        choices=[
            "Basic Django",
            "Django + Postgres",
            "Django + RestFramework",
            "Django + Channels",
        ],
        style=custom_style,
    ).ask()

    db_details = None
    if project_type == "Django + Postgres":
        console.print(
            Panel.fit(
                "[bold red]⚠ WARNING: Make sure you create your PostgreSQL database before proceeding! "
                "This tool will run migrations automatically, and if the database does not exist, it will fail.[/bold red]",
                style="bold red",
                border_style="red",
            )
        )

        db_details = {
            "name": questionary.text(
                "Enter the PostgreSQL database name (default: mydb)", style=custom_style
            ).ask()
            or "mydb",
            "user": questionary.text(
                "Enter the PostgreSQL user (default: postgres)", style=custom_style
            ).ask()
            or "postgres",
            "password": questionary.password(
                "Enter the PostgreSQL password (default: admin)", style=custom_style
            ).ask()
            or "admin",
            "host": questionary.text(
                "Enter the PostgreSQL host (default: localhost)", style=custom_style
            ).ask()
            or "localhost",
            "port": questionary.text(
                "Enter the PostgreSQL port (default: 5432)", style=custom_style
            ).ask()
            or "5432",
        }

        console.print(
            "[bold green]✔ Database Configuration Complete! Make sure your database is set up before proceeding.[/bold green]"
        )

    return project_name, app_name, username, password, project_type, db_details


def main():
    project_name, app_name, username, password, project_type, db_details = user_prompt()
    requirements = create_requirements(project_type)
    setting_up(
        project_name,
        app_name,
        requirements,
        project_type,
        db_details,
        username,
        password,
    )


if __name__ == "__main__":
    main()
