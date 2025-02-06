from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="m4rtin",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[],
    author="Martín Martín",
    description="Una biblioteca para consultar cursos de Hack4u",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io"
)
