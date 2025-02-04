from setuptools import find_packages, setup

setup(
    name="pipg",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pipg = pipg.cli:main",
        ],
    },
    author="Guilherme Gonçalves Soares",
    author_email="guilherme16.gon@gmail.com",
    description="Wrapper para pip que automatiza a instalação, remoção e gerenciamento de dependências em arquivos de requirements.",
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
