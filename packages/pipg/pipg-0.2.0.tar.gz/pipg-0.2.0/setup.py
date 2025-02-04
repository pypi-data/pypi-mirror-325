from setuptools import find_packages, setup

setup(
    name="pipg",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pipg = pipg.cli:main",
        ],
    },
    author="Guilherme Gonçalves Soares",
    author_email="guilherme16.gon@gmail.com",
    description="Um wrapper simples para o pip que instala e já escreve o nome e a versão do pacote no requirements.txt",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GuilhermeGonSoares/pipg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
