import pytest
import tkinter as tk
import time
import itertools
from threading import Thread
from unittest.mock import patch, MagicMock

from login_canaime.model import CanaimeLoginModel, LOGIN_URL
from login_canaime.view import CanaimeLoginView
from login_canaime.controller import CanaimeLoginController

# =============================================================================
# Testes para o Model
# =============================================================================

def test_perform_login_raises_value_error_on_empty_credentials():
    """
    Verifica se uma ValueError é lançada quando usuário ou senha estão vazios.
    """
    model = CanaimeLoginModel()
    with pytest.raises(ValueError):
        model.perform_login("", "senha_qualquer")
    with pytest.raises(ValueError):
        model.perform_login("usuario_qualquer", "")

@patch("login_canaime.model.sync_playwright")
def test_perform_login_success(mock_sync_playwright):
    """
    Simula um login de sucesso:
      - Mocka o fluxo do Playwright,
      - Simula que a contagem de imagens na página é >= 4,
      - Verifica se o método perform_login retorna True.
    """
    # Cria mocks para a cadeia de chamadas do Playwright
    mock_playwright_instance = MagicMock()
    mock_sync_playwright.return_value.__enter__.return_value = mock_playwright_instance

    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_playwright_instance.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    # Simula que a contagem de imagens é 4 (login bem-sucedido pela heurística)
    mock_page.locator.return_value.count.return_value = 4

    model = CanaimeLoginModel()
    result = model.perform_login("usuario", "senha")
    assert result is True

@patch("login_canaime.model.sync_playwright")
def test_perform_login_failure(mock_sync_playwright):
    """
    Simula um login que falha:
      - Mocka o fluxo do Playwright,
      - Simula que a contagem de imagens é < 4,
      - Verifica se o método perform_login retorna False.
    """
    mock_playwright_instance = MagicMock()
    mock_sync_playwright.return_value.__enter__.return_value = mock_playwright_instance

    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_playwright_instance.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    # Simula que a contagem de imagens é 2 (falha no login)
    mock_page.locator.return_value.count.return_value = 2

    model = CanaimeLoginModel()
    result = model.perform_login("usuario_invalido", "senha_invalida")
    assert result is False

@patch("login_canaime.model.sync_playwright")
def test_login_js_images_disabled_returns_page(mock_sync_playwright):
    """
    Simula o fluxo de login com JavaScript desabilitado e imagens bloqueadas,
    verificando se o método retorna uma instância de Page.
    """
    mock_playwright_instance = MagicMock()
    mock_sync_playwright.return_value.__enter__.return_value = mock_playwright_instance

    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()

    mock_playwright_instance.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    model = CanaimeLoginModel()
    page = model.login_js_images_disabled("usuario", "senha")
    assert page is mock_page

# =============================================================================
# Testes para a View
# =============================================================================

@pytest.fixture
def tk_root():
    """
    Cria (e destrói) uma instância do Tk para testes da interface.
    """
    root = tk.Tk()
    yield root
    root.destroy()

def test_get_username_and_password(tk_root):
    """
    Verifica se os métodos get_username e get_password retornam os valores esperados.
    """
    view = CanaimeLoginView(tk_root)
    view.username_entry.insert(0, "teste_usuario")
    view.password_entry.insert(0, "teste_senha")
    assert view.get_username() == "teste_usuario"
    assert view.get_password() == "teste_senha"

def test_disable_enable_login_button(tk_root):
    """
    Verifica se os métodos disable_login_button e enable_login_button alteram corretamente o estado do botão.
    """
    view = CanaimeLoginView(tk_root)
    view.disable_login_button()
    assert view.login_button["state"] == tk.DISABLED
    view.enable_login_button()
    assert view.login_button["state"] == tk.NORMAL

def test_set_status_message(tk_root):
    """
    Verifica se o método set_status_message atualiza o label de status corretamente.
    """
    view = CanaimeLoginView(tk_root)
    mensagem = "Status de teste"
    view.set_status_message(mensagem)
    assert view.status_label["text"] == mensagem

def test_loading_animation(tk_root):
    """
    Verifica se a animação de carregamento inicia e para conforme esperado.
    """
    view = CanaimeLoginView(tk_root)
    view.start_loading_animation()
    # Aguarda um pouco para a animação iniciar
    time.sleep(0.5)
    assert view.is_running is True
    view.stop_loading_animation()
    time.sleep(0.3)
    assert view.is_running is False

# =============================================================================
# Testes para o Controller
# =============================================================================

def test_on_enter_triggers_login_process(tk_root):
    """
    Verifica se o método on_enter invoca o início do processo de login.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)
    chamado = False

    def fake_start_login_process():
        nonlocal chamado
        chamado = True

    controller.start_login_process = fake_start_login_process
    # Cria um evento dummy
    evento = tk.Event()
    controller.on_enter(evento)
    assert chamado is True

def test_start_login_process_in_controller(tk_root, monkeypatch):
    """
    Verifica se o método start_login_process:
      - Desabilita o botão de login,
      - Atualiza o status da view,
      - Inicia a animação de carregamento,
      - E inicia a thread para executar o login.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)

    # Variável para confirmar que _execute_login foi chamado
    chamado_execute_login = False
    def fake_execute_login():
        nonlocal chamado_execute_login
        chamado_execute_login = True
    monkeypatch.setattr(controller, "_execute_login", fake_execute_login)

    # Utiliza um dicionário para monitorar as chamadas da view
    estado = {"disable": False, "status": None, "start_anim": False}
    def fake_disable():
        estado["disable"] = True
    def fake_set_status(msg: str):
        estado["status"] = msg
    def fake_start_anim():
        estado["start_anim"] = True

    controller.view.disable_login_button = fake_disable
    controller.view.set_status_message = fake_set_status
    controller.view.start_loading_animation = fake_start_anim

    controller.start_login_process()
    # Aguarda um curto período para a thread ser iniciada
    time.sleep(0.2)
    assert estado["disable"] is True
    assert estado["status"] == "Realizando login..."
    assert estado["start_anim"] is True
    assert chamado_execute_login is True

def test_login_success_in_controller(tk_root):
    """
    Verifica se o método _login_success do controller:
      - Interrompe a animação de carregamento,
      - Atualiza o status com mensagem de sucesso,
      - Agenda o fechamento da janela.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)
    chamadas = []

    controller.view.stop_loading_animation = lambda: chamadas.append("stop_loading_animation")
    controller.view.set_status_message = lambda msg: chamadas.append(("set_status_message", msg))
    # Substitui o método after para execução imediata e registro da chamada
    tk_root.after = lambda delay, func: (chamadas.append(("after", delay)), func())

    controller._login_success()

    assert chamadas[0] == "stop_loading_animation"
    assert chamadas[1] == ("set_status_message", "Login efetuado com sucesso!")
    assert chamadas[2][0] == "after"
    assert chamadas[2][1] == 1000

def test_login_error_in_controller(tk_root):
    """
    Verifica se o método _login_error do controller:
      - Interrompe a animação de carregamento,
      - Atualiza o status com a mensagem de erro,
      - Habilita novamente o botão de login.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)
    chamadas = []

    controller.view.stop_loading_animation = lambda: chamadas.append("stop_loading_animation")
    controller.view.set_status_message = lambda msg: chamadas.append(("set_status_message", msg))
    controller.view.enable_login_button = lambda: chamadas.append("enable_login_button")

    mensagem_erro = "Erro de teste"
    controller._login_error(mensagem_erro)
    assert chamadas[0] == "stop_loading_animation"
    assert chamadas[1] == ("set_status_message", mensagem_erro)
    assert chamadas[2] == "enable_login_button"

# =============================================================================
# Testes de Integração
# =============================================================================

def test_full_login_flow_success(tk_root, monkeypatch):
    """
    Teste de integração que simula o fluxo completo de login com sucesso:
      - O usuário insere as credenciais na interface,
      - O controller inicia o processo de login,
      - O model executa o login simulando sucesso,
      - A view é atualizada e, normalmente, a janela seria fechada.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)

    # Preenche os campos da view com credenciais válidas
    controller.view.username_entry.insert(0, "usuario")
    controller.view.password_entry.insert(0, "senha")

    # Simula um login bem-sucedido substituindo o método do model
    monkeypatch.setattr(controller.model, "perform_login", lambda u, p: True)
    # Substitui _login_success para apenas registrar a chamada sem destruir a janela
    login_success_chamado = False
    def fake_login_success():
        nonlocal login_success_chamado
        login_success_chamado = True
    monkeypatch.setattr(controller, "_login_success", fake_login_success)

    controller.start_login_process()
    time.sleep(0.5)  # aguarda o processamento em thread
    assert login_success_chamado is True

def test_full_login_flow_failure(tk_root, monkeypatch):
    """
    Teste de integração que simula o fluxo completo de login com falha:
      - O usuário insere credenciais inválidas,
      - O controller inicia o processo de login,
      - O model executa o login simulando falha,
      - A view é atualizada com a mensagem de erro e o botão é reabilitado.
    """
    controller = CanaimeLoginController(tk_root, test_mode=True)

    controller.view.username_entry.insert(0, "usuario_invalido")
    controller.view.password_entry.insert(0, "senha_invalida")

    monkeypatch.setattr(controller.model, "perform_login", lambda u, p: False)
    erro_recebido = None
    def fake_login_error(msg: str):
        nonlocal erro_recebido
        erro_recebido = msg
    monkeypatch.setattr(controller, "_login_error", fake_login_error)

    controller.start_login_process()
    time.sleep(0.5)
    assert erro_recebido == "Usuário ou senha inválidos."
