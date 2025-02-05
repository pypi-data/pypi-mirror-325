# pipg - Wrapper para Pip

`pipg` é um wrapper para `pip` que facilita a instalação e remoção de pacotes Python, mantendo automaticamente arquivos de dependências organizados.

## 🚀 Funcionalidades
- Instala pacotes com `pipg install <pacote> [--group <prod|dev|test>]`.
- Remove pacotes com `pipg uninstall <pacote>`.
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

### ✅ Instalar um pacote
```sh
pipg install fastapi --group dev
```
Isso instalará o pacote `fastapi` e o registrá em `requirements-dev.txt`. Se `--group` não for especificado, ele será registrado em `requirements.txt`.

### ❌ Desinstalar um pacote
```sh
pipg uninstall fastapi
```
Isso removerá o `fastapi` do ambiente e também de **todos os arquivos** de requirements (`requirements.txt`, `requirements-dev.txt`, `requirements-test.txt`).

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
