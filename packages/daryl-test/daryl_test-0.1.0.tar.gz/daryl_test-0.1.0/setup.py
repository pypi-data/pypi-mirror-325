from setuptools import setup, find_packages

# Read README contents
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="daryl_test",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Daryl Esquivel",
    description="Una biblioteca para consultar cursos de hack4u.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io/"
)
