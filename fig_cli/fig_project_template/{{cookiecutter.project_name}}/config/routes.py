from pathlib import Path
from flask import Blueprint, render_template

# Path Resolution
HERE = Path(".")
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_FOLDER = BASE_DIR.joinpath("public")
STATIC_FOLDER = BASE_DIR.joinpath("public/assets")
MODELS_DIR = BASE_DIR.joinpath("{{cookiecutter.project_name}}", "models")

# Blueprints
VIEWS = Blueprint(__file__, "views",
                  template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
API = Blueprint(__file__, "api", url_prefix="/api")


@VIEWS.route("/")
def handle_get_index():
    project_name = '{{cookiecutter.project_name}}'
    all_models = [m for m in MODELS_DIR.glob(
        "*.py") if m.is_file()]
    return render_template("index.html", project_name=project_name, all_models=all_models)


@VIEWS.route('/', defaults={'path': ''})
@VIEWS.route("/<path:path>")
def handle_not_found(path):
    return render_template("404.html", path=path)
