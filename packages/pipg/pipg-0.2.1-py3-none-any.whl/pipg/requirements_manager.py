import os
from utils import colored_text


def update_requirements(package_name, version, requirements_file):
    package_entry = f"{package_name}=={version}"

    if not os.path.exists(requirements_file):
        with open(requirements_file, "w") as f:
            f.write(package_entry + "\n")
        print(
            colored_text(
                f"PACOTE: {package_entry} registrado no {requirements_file}", "green"
            )
        )
        return

    with open(requirements_file, "r") as f:
        lines = f.readlines()

    updated = False
    with open(requirements_file, "w") as f:
        for line in lines:
            if line.startswith(f"{package_name}=="):
                f.write(package_entry + "\n")
                updated = True
            else:
                f.write(line)
        if not updated:
            f.write(package_entry + "\n")
            print(
                colored_text(
                    f"PACOTE: {package_entry} registrado no {requirements_file}",
                    "green",
                )
            )
        else:
            print(
                colored_text(
                    f"PACOTE: {package_entry} atualizado no {requirements_file}",
                    "yellow",
                )
            )


def remove_from_requirements(package_name, requirements_file):
    if not os.path.exists(requirements_file):
        return

    try:
        with open(requirements_file, "r") as f:
            lines = f.readlines()

        with open(requirements_file, "w") as f:
            for line in lines:
                if not line.startswith(f"{package_name}=="):
                    f.write(line)
        print(
            colored_text(
                f"PACOTE: {package_name} removido do {requirements_file}", "green"
            )
        )
    except IOError:
        print(colored_text(f"Erro ao acessar o arquivo {requirements_file}", "red"))
