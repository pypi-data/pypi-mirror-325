import argparse
import sys
from pipg.package_manager import install_package, uninstall_package
from pipg.utils import colored_text


def main():
    parser = argparse.ArgumentParser(description="Gerenciador de pacotes com pip.")

    parser.add_argument(
        "command", choices=["install", "uninstall"], help="Comando a ser executado"
    )

    parser.add_argument(
        "--group",
        choices=["prod", "dev", "test"],
        default="prod",
        help="Define o grupo de instalação (padrão: prod).",
    )

    parser.add_argument(
        "packages", nargs="+", help="Nome do pacote a ser instalado/desinstalado"
    )

    args = parser.parse_args()

    if args.command == "uninstall" and "--group" in sys.argv:
        print(
            colored_text(
                "Erro: O comando 'uninstall' remove o pacote globalmente. Remove o registro de todos os requirements. "
                "A flag '--group' não é permitida.",
                "red",
            )
        )
        sys.exit(1)

    if args.command == "install":
        for package in args.packages:
            install_package(package, args.group)
    elif args.command == "uninstall":
        for package in args.packages:
            uninstall_package(package)
    else:
        print(
            colored_text(
                "Comando não reconhecido. Apenas 'install' e 'uninstall' são suportados.",
                "red",
            )
        )


if __name__ == "__main__":
    main()
