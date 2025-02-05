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
            [sys.executable, "-m", "pip", "show", package_name],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None
