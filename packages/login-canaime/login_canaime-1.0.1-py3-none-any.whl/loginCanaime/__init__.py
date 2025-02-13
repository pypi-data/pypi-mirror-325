"""
Pacote loginCanaime
--------------------
Este pacote fornece as funcionalidades para o login no Sistema Canaimé,
integrando Model, View e Controller em uma interface simples e reutilizável.

Exemplo de uso:
    from loginCanaime import Login

    # Para realizar o login e obter a página logada:
    page = Login.run(test_mode=False)

    # Para obter as credenciais (modo desenvolvimento):
    credentials = Login.get_credentials(test_mode=False)
"""

__version__ = "0.1.0"

# Importa a classe Login do módulo main.py
from .main import Login
