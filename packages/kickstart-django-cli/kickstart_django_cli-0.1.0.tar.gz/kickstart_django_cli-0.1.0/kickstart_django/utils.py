from rich.console import Console
import re
import sys


console = Console()


def validate__name(text: str) -> bool:
    """
    Validates Django project name or app name against the following rules:
    - Allow empty input to accept default values.
    - Must start with a letter or underscore if provided.
    - Can only contain letters, numbers, and underscores.
    - Cannot be a Python reserved word if provided.
    """
    if not text.strip():  # Allow empty input for defaults
        return True

    python_keywords = {
        "False",
        "None",
        "True",
        "and",
        "as",
        "assert",
        "async",
        "await",
        "break",
        "class",
        "continue",
        "def",
        "del",
        "elif",
        "else",
        "except",
        "finally",
        "for",
        "from",
        "global",
        "if",
        "import",
        "in",
        "is",
        "lambda",
        "nonlocal",
        "not",
        "or",
        "pass",
        "raise",
        "return",
        "try",
        "while",
        "with",
        "yield",
    }

    if not (text[0].isalpha() or text[0] == "_"):
        return "❌ Name must start with a letter or underscore"

    if not all(c.isalnum() or c == "_" for c in text):
        return "❌ Name can only contain letters, numbers, and underscores"

    if text in python_keywords:
        return "❌ Name cannot be a Python reserved word"

    return True


def password_validator(password: str) -> bool:
    """
    Validates password with basic criteria:
    - Allow empty input to accept default values.
    - Password must be at least 6 characters if provided.
    """
    if not password.strip():  # Allow empty input for defaults
        return True

    if len(password) < 6:
        return "❌ Password must be at least 6 characters long"

    return True


def create_requirements(project_type):
    match project_type:
        case "Basic Django":
            # Basic Django project dependencies
            requirements = [
                "Django>=4.0",  # Default Django version
                "python-dotenv",
            ]

        case "Django + Postgres":
            # Determine the appropriate psycopg2 package based on OS
            if sys.platform == "win32":
                # On Windows, use the binary version
                requirements = [
                    "Django>=4.0",  # Django version
                    "psycopg2-binary>=2.9",
                    "python-dotenv",  # Binary version for Windows
                ]
            elif sys.platform == "darwin":
                # On macOS, use the regular psycopg2
                requirements = [
                    "Django>=4.0",  # Django version
                    "psycopg2>=2.9",
                    "python-dotenv",  # Regular psycopg2 for macOS
                ]
            else:
                # Assume Linux or other platforms, use psycopg2
                requirements = [
                    "Django>=4.0",  # Django version
                    "psycopg2>=2.9",
                    "python-dotenv",  # psycopg2 for Linux and other platforms
                ]

        case "Django + RestFramework":
            # Django with Django REST framework dependencies
            requirements = [
                "Django>=4.0",  # Django version
                "djangorestframework>=3.14",
                "python-dotenv",  # REST Framework
                "coreapi>=2.3.3",
            ]
        case "Django + Channels":
            requirements = [
                "Django>=4.0",  # Default Django version
                "python-dotenv",
                "channels>=4.1.0",
                "daphne>=4.1.0",
                "websockets>=12.0",
            ]

        case _:
            # Default case, handle unknown project types
            console.print(
                f"[bold red]Unknown project type: {project_type}. Defaulting to 'Basic Django' dependencies.[/bold red]"
            )
            requirements = [
                "Django>=4.0",  # Default to basic Django if project type is unknown
                "python-dotenv",
            ]

    return requirements
