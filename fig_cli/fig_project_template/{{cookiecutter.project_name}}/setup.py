from setuptools import find_packages, setup


setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    install_requires=["Flask", "FlaskCors", "autopep8", "pylint"]
)
