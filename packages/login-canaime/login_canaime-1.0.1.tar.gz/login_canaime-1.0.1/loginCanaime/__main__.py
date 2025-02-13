"""
Módulo __main__
----------------
Ponto de entrada do pacote loginCanaime.
Quando o pacote é executado via 'python -m loginCanaime', este módulo é chamado.
"""

from .main import Login

if __name__ == "__main__":
    Login.run(test_mode=False)
