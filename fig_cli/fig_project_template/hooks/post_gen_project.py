import pathlib
import subprocess

HERE = pathlib.Path('.')
REQUIREMENTS_TXT = (HERE / "requirements.txt")


def pip_install_required_elements():
    # TODO: Create Virtual Env for pip install
    subprocess.check_call(["python", "-m", "pip",
                           "install", "-r", REQUIREMENTS_TXT])


def git_init():
    subprocess.check_call(["git", "init"])


def post_gen():
    print("Installing project depedencies")
    pip_install_required_elements()
    git_init()


post_gen()
