from setuptools import setup, find_packages
from pathlib import Path

# Ler README com encoding correto
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="apibrain-sdk",
    version="0.1.0",
    author="System32miro",
    author_email="seu.email@exemplo.com",
    description="SDK para criar APIs auto-descritivas compatíveis com agentes IA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/system32miro/apibrain-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fastapi>=0.68.0",
        "pydantic>=1.8.0"
    ]
) 