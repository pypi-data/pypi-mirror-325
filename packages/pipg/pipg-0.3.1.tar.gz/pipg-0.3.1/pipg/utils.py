import os
import subprocess
import sys


def colored_text(text, color):
    colors = {
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "reset": "\033[0m",
    }
    return f"{colors[color]}{text}{colors['reset']}"


def get_python_executable():
    virtual_env = os.environ.get("VIRTUAL_ENV")
    print(f"VIRTUAL ENV ENCONTRADO: {virtual_env}")
    if virtual_env:
        if os.name == "nt":
            python_path = os.path.join(virtual_env, "Scripts", "python.exe")
        else:
            python_path = os.path.join(virtual_env, "bin", "python")
        if os.path.exists(python_path):
            return python_path
    return sys.executable


def is_package_installed(package_name):
    return bool(get_installed_package(package_name).strip())


def get_installed_version(package_name):
    result = get_installed_package(package_name).splitlines()
    for line in result:
        if line.startswith("Version:"):
            return line.split()[1]


def get_installed_package(package_name: str) -> str | None:
    try:
        result = subprocess.run(
            [get_python_executable(), "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None
