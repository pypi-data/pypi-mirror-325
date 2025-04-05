from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kickstart-django-cli",
    version="0.1.0",
    packages=find_packages(include=["kickstart_django", "kickstart_django.*"]),
    install_requires=["rich", "questionary", "astor"],
    entry_points={
        "console_scripts": [
            "kickstart-django=kickstart_django.cli:main",
        ],
    },
    author="Remith R Nair",
    author_email="nair.remith@gmail.com",
    description="A simple CLI tool to scaffold Django projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Remithrn/django-kickstart-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
