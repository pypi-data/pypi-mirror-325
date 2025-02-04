import subprocess
import sys
from utils import colored_text, is_package_installed, get_installed_version
from requirements_manager import update_requirements, remove_from_requirements

GROUP_REQUIREMENTS = {
    "prod": "requirements.txt",
    "dev": "requirements-dev.txt",
    "test": "requirements-test.txt",
}


def install_package(package_name, group="prod"):
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name], check=True
        )
        print(colored_text(f"PACOTE: {package_name} instalado com sucesso!", "green"))
    except subprocess.CalledProcessError:
        print(colored_text(f"Erro ao instalar {package_name}", "red"))
        return

    package_name = package_name.split("==")[0]
    version = get_installed_version(package_name)

    if version:
        update_requirements(package_name, version, GROUP_REQUIREMENTS[group])
    else:
        print(colored_text(f"Erro ao obter a versão do {package_name}", "red"))


def uninstall_package(package_name):
    """Desinstala um pacote do ambiente e remove de todos os arquivos de requirements"""
    package_name = package_name.split("==")[0]
    if not is_package_installed(package_name):
        print(colored_text(f"{package_name} não está instalado.", "yellow"))
        return

    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "uninstall", "-y", package_name], check=True
        )
        print(
            colored_text(f"PACOTE: {package_name} desinstalado com sucesso!", "green")
        )
    except subprocess.CalledProcessError:
        print(colored_text(f"Erro ao desinstalar {package_name}", "red"))
        return

    # Remover o pacote de TODOS os arquivos de requirements
    for group_file in GROUP_REQUIREMENTS.values():
        remove_from_requirements(package_name, group_file)
