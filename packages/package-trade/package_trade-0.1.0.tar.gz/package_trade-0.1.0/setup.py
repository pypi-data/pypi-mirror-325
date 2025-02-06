from setuptools import setup, find_packages
import os

# Caminho absoluto para o requirements.txt
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Lê o conteúdo do requirements.txt
with open(requirements_path, "r") as f:
    requirements = f.read().splitlines()

# Lê o conteúdo do README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="package_trade",
    version="0.1.0",
    author="Danrley",
    author_email="seu_email@example.com",  # Preencha com seu email
    description="Trade program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanrleyS/Machine_learn_prever_valor_acoes",
    packages=find_packages(),
    install_requires=requirements,
    license="MIT",
)
