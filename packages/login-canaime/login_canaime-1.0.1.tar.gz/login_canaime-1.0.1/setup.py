from setuptools import setup, find_packages

setup(
    name="login-canaime",  # Nome de distribuição usado no pip
    version="1.0.1",
    description="Sistema de login Canaimé para gerenciamento de unidades prisionais.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Anderson Assunção",
    author_email="andersongomesrr@hotmail.com",
    url="https://github.com/A-Assuncao/login-canaime_project",
    packages=find_packages(),  # Isso encontrará o pacote "loginCanaime"
    install_requires=[
        "PySide6",
        "playwright",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)