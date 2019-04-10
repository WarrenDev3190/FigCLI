import fig_cli
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setup(
    name="FigCLI",
    version=fig_cli.__version__,
    description="The batteries included, convention over configuration, python, data science, application framework",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Fig Development Team",
    author_email="figframework@gmail.com",
    license="MIT",
    classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "cookiecutter",
        "click",
        "PyInquirer"
    ],
    entry_points={
        "console_scripts": [
            "fig=fig_cli.__main__:fig"
        ]
    }
)
