# pipg - Wrapper para Pip

`pipg` é um wrapper para `pip` que facilita a instalação e remoção de pacotes Python, mantendo automaticamente arquivos de dependências organizados.

## 🚀 Funcionalidades
- Instala um ou mais pacotes com `pipg install <pacote1> <pacote2> ... [--group <prod|dev|test>]`.
- Remove um ou mais pacotes com `pipg uninstall <pacote1> <pacote2> ...`.
- Atualiza automaticamente o arquivo de dependências correto (`requirements.txt`, `requirements-dev.txt`, `requirements-test.txt`).
- Remove pacotes desinstalados de **todos** os arquivos de requirements.
- Mensagens coloridas para melhor visualização dos status.

## 📚 Instalação
Para instalar o `pipg`:

```sh
pip install pipg
```

Ou, para instalar localmente:

```sh
pip install .
```

## 🛠 Uso

### ✅ Instalar um ou mais pacotes
```sh
pipg install fastapi uvicorn requests --group dev
```
Isso instalará os pacotes `fastapi`, `uvicorn` e `requests` e os registrará em `requirements-dev.txt`. Se `--group` não for especificado, os pacotes serão registrados em `requirements.txt`.

### ❌ Desinstalar um ou mais pacotes
```sh
pipg uninstall fastapi uvicorn requests
```
Isso removerá `fastapi`, `uvicorn` e `requests` do ambiente e também de **todos os arquivos** de requirements (`requirements.txt`, `requirements-dev.txt`, `requirements-test.txt`).

## 🏢 Estrutura do Projeto
```
pipg/
│── pipg/
│   │── __init__.py
│   │── cli.py
│   │── package_manager.py
│   │── requirements_manager.py
│   │── utils.py
│── setup.py
│── README.md
│── pyproject.toml
```

## 🤝 Contribuição
1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin minha-feature`).
5. Abra um Pull Request.

