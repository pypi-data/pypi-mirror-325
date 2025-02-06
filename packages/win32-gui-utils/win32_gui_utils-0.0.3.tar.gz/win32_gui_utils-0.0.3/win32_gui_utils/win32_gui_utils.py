# pylint: disable=W0719, W0707, W0718,I1101, W0601, C0411, C0103, C0301, W0613

"""
Módulo: win32_gui_utils

Descrição:
    Este módulo fornece funcionalidades para interagir com elementos da interface gráfica
    do Windows por meio das APIs do win32. São implementadas funções que permitem localizar
    janelas, obter e manipular handles de controles, simular cliques e outras interações,
    enviar mensagens e extrair propriedades de controles dentro de janelas. Essas rotinas
    facilitam a automação e o controle de aplicativos baseados em janelas no ambiente Windows.

Dependências:
    - pywin32: Fornece acesso às APIs do Windows (win32gui, win32con, win32api).
    - time, ctypes: Módulos padrão do Python para controle de tempo e manipulação de buffers.
"""

import win32gui
import win32con
import time
import win32api
import ctypes
import json

def find_window(window_name, max_attempts=3, wait_time=2):
    """
    Localiza uma janela pelo seu nome (título), realizando várias tentativas se necessário.

    Args:
        window_name (str): Nome/título da janela a ser localizada.
        max_attempts (int, opcional): Número máximo de tentativas. Padrão é 3.
        wait_time (float, opcional): Intervalo em segundos entre as tentativas. Padrão é 2.

    Returns:
        int: Handle (identificador) da janela, se localizada.

    Raises:
        Exception: Se a janela não for encontrada após o número máximo de tentativas.
    """
    for attempt in range(max_attempts):
        handle = win32gui.FindWindow(None, window_name)
        if handle != 0:  # Janela encontrada
            print(f"Janela encontrada na tentativa {attempt + 1}: Handle = {hex(handle)}")
            return handle

        print(f"Tentativa {attempt + 1} falhou. Aguardando {wait_time} segundos...")
        time.sleep(wait_time)

    raise Exception(f"Janela '{window_name}' não encontrada após {max_attempts} tentativas.")

def enum_child_windows_callback(hwnd, target_id):
    """
    Callback para ser utilizado na enumeração de janelas filhas.
    Verifica se o controle possui o ID desejado e, em caso positivo, o adiciona a uma lista global.

    Args:
        hwnd (int): Handle da janela filha atual.
        target_id (int): ID do controle buscado.
    """
    control_id = win32gui.GetDlgCtrlID(hwnd)
    if control_id == target_id:
        print(f"Handle encontrado para ID {target_id}: {hex(hwnd)}")
        extra.append(hwnd)  # Armazena o handle encontrado


def get_handle_by_id(hwnd, target_id):
    """
    Obtém o handle de um controle especificado pelo ID dentro de uma janela (via enumeração).

    Args:
        hwnd (int): Handle da janela pai onde o controle será procurado.
        target_id (int): ID do controle desejado.

    Returns:
        int ou None: O handle do controle, se encontrado; caso contrário, None.
    """
    global extra
    extra = []  # Lista para acumular os handles encontrados
    win32gui.EnumChildWindows(
        hwnd, lambda hwnd, _: enum_child_windows_callback(hwnd, target_id), None
    )
    return extra[0] if extra else None


def wait_for_control(hwnd, target_id, timeout=10, poll_interval=0.5):
    """
    Aguarda até que um controle com o target_id seja encontrado e esteja pronto para 
    interação. O controle é considerado "pronto" se estiver visível, habilitado e possuir
    dimensões válidas.

    Args:
        hwnd (int): Handle da janela pai na qual procurar.
        target_id (int): ID do controle desejado.
        timeout (float, opcional): Tempo máximo de espera em segundos. Padrão é 10.
        poll_interval (float, opcional): Intervalo entre as verificações em segundos. Padrão é 0.5.

    Returns:
        int: Handle do controle assim que estiver pronto.

    Raises:
        Exception: Se o controle não for encontrado ou não estiver pronto dentro do tempo especificado.
    """
    start_time = time.time()
    attempts = 0
    while time.time() - start_time < timeout:
        attempts += 1
        handle = get_handle_by_id(hwnd, target_id)
        if handle is not None:
            # Verifica se o controle está visível, habilitado e possui tamanho válido
            if win32gui.IsWindowVisible(handle) and win32gui.IsWindowEnabled(handle):
                rect = win32gui.GetWindowRect(handle)
                width = rect[2] - rect[0]
                height = rect[3] - rect[1]
                if width > 0 and height > 0:
                    print(f"Controle encontrado e pronto após {attempts} tentativas.")
                    return handle
        time.sleep(poll_interval)

    raise Exception(
        f"Controle com ID {target_id} não encontrado ou não está pronto após {attempts} tentativas em {timeout} segundos."
    )


def is_valid_window(handle):
    """
    Verifica se o handle fornecido corresponde a uma janela válida.

    Args:
        handle (int): Handle da janela a ser validada.

    Returns:
        bool: True se a janela é válida; caso contrário, False.
    """
    return win32gui.IsWindow(handle)


def get_handle_from_hex(hex_handle):
    """
    Converte uma representação hexadecimal do handle (seja em formato string ou int)
    para um inteiro.

    Args:
        hex_handle (str ou int): Representação do handle.

    Returns:
        int: Handle convertido para inteiro.

    Raises:
        ValueError: Se o valor fornecido não puder ser convertido.
    """
    try:
        if isinstance(hex_handle, str):
            return int(hex_handle, 16)
        return hex_handle
    except ValueError as e:
        raise ValueError(f"Handle inválido: {hex_handle}. Erro: {e}")


def get_edit_text(hwnd_edit):
    """
    Recupera o texto de um controle de edição (EDIT) identificado pelo seu handle.

    Args:
        hwnd_edit (int): Handle do controle de edição.

    Returns:
        str: Texto contido no controle.
    """
    length = win32gui.SendMessage(hwnd_edit, win32con.WM_GETTEXTLENGTH, 0, 0)
    buffer = ctypes.create_unicode_buffer(length + 1)
    win32gui.SendMessage(hwnd_edit, win32con.WM_GETTEXT, length + 1, buffer)
    return buffer.value


def click_button_by_handle(hwnd):
    """
    Simula um clique do mouse no centro do controle especificado pelo seu handle.

    Args:
        hwnd (int): Handle do controle onde o clique será simulado.

    Raises:
        Exception: Se o handle for inválido ou a janela não existir.
    """
    if not win32gui.IsWindow(hwnd):
        raise Exception("Handle inválido ou janela não existe")

    rect = win32gui.GetWindowRect(hwnd)
    center_x = (rect[0] + rect[2]) // 2
    center_y = (rect[1] + rect[3]) // 2

    win32api.SetCursorPos((center_x, center_y))
    time.sleep(0.1)  # Aguarda o posicionamento do cursor
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, center_x, center_y, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, center_x, center_y, 0, 0)


def click_button(hex_handle):
    """
    Converte um handle em formato hexadecimal para inteiro e simula um clique no centro
    do controle correspondente.

    Args:
        hex_handle (str ou int): Handle do controle (em formato hexadecimal ou inteiro).

    Raises:
        Exception: Se ocorrer algum erro durante a conversão ou se o controle for inválido.
    """
    try:
        handle = get_handle_from_hex(hex_handle)
        if not win32gui.IsWindow(handle):
            raise Exception("Handle inválido ou janela não existe")
        click_button_by_handle(handle)
    except Exception as e:
        raise Exception(f"Erro ao clicar no botão: {e}")


def right_click(hex_handle):
    """
    Simula um clique com o botão direito do mouse no controle especificado por um handle.

    Args:
        hex_handle (str ou int): Handle do controle (em formato hexadecimal ou inteiro).

    Raises:
        Exception: Se o handle for inválido ou a janela não existir.
    """
    try:
        handle = get_handle_from_hex(hex_handle)
        if not is_valid_window(handle):
            raise Exception("Handle inválido ou janela não existe")
        win32gui.SendMessage(handle, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, 0)
        time.sleep(0.05)
        win32gui.SendMessage(handle, win32con.WM_RBUTTONUP, 0, 0)
    except Exception as e:
        raise Exception(f"Erro ao clicar com botão direito: {e}")


def write_text(hex_handle, text):
    """
    Envia uma string de texto para um controle, utilizando a mensagem WM_SETTEXT.

    Args:
        hex_handle (str ou int): Handle do controle (em formato hexadecimal ou inteiro).
        text (str): Texto a ser definido no controle.

    Raises:
        Exception: Se o handle for inválido ou ocorrer erro ao enviar o texto.
    """
    try:
        if hex_handle:
            win32gui.SendMessage(hex_handle, win32con.WM_SETTEXT, 0, text)
        else:
            raise Exception(f"Input com handle: {hex_handle} não encontrado!")
    except Exception as e:
        raise Exception(f"Erro ao escrever texto: {e}")


def get_control_properties(parent_handle, inspect: bool = False):
    """
    Coleta e retorna diversas propriedades dos controles filhos de uma janela especificada.

    As propriedades coletadas incluem:
        - handle: Identificador do controle.
        - auto_id: Identificador único do controle.
        - text: Texto associado ao controle.
        - class_name: Nome da classe do controle.
        - rect: Tupla (left, top, right, bottom) com a posição e dimensões.
        - style: Estilo do controle (GWL_STYLE).
        - ex_style: Estilos estendidos (GWL_EXSTYLE).
        - visible: Indicador se o controle está visível.
        - enabled: Indicador se o controle está habilitado.
        - parent: Handle da janela pai.

    Args:
        parent_handle (int): Handle da janela a ser inspecionada.

    Returns:
        list: Lista de dicionários, onde cada dicionário contém as propriedades de um controle.
    """
    controles = []

    def callback(hwnd, lParam):
        try:
            auto_id = win32gui.GetDlgCtrlID(hwnd)
            text = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
            visible = win32gui.IsWindowVisible(hwnd)
            enabled = win32gui.IsWindowEnabled(hwnd)
            parent = win32gui.GetParent(hwnd)

            controle_info = {
                "handle": hwnd,
                "auto_id": auto_id,
                "text": text,
                "class_name": class_name,
                "rect": rect,
                "style": style,
                "ex_style": ex_style,
                "visible": visible,
                "enabled": enabled,
                "parent": parent,
            }
            controles.append(controle_info)
        except Exception as e:
            print(f"Erro ao obter informações do controle {hex(hwnd)}: {e}")
        return True

    win32gui.EnumChildWindows(parent_handle, callback, None)
    if inspect:
        print(json.dumps(controles, indent=4, ensure_ascii=False))
    return controles


def select_combo_item(combo_hwnd, index):
    """
    Seleciona um item de um ComboBox com base no índice fornecido, utilizando a mensagem
    CB_SETCURSEL, e envia uma notificação (CBN_SELCHANGE) para o dono do controle.

    Args:
        combo_hwnd (int): Handle do ComboBox.
        index (int): Índice do item a ser selecionado.
    """
    win32gui.SendMessage(combo_hwnd, win32con.CB_SETCURSEL, index, 0)
    parent_hwnd = win32gui.GetParent(combo_hwnd)
    ctrl_id = win32gui.GetDlgCtrlID(combo_hwnd)
    win32gui.SendMessage(
        parent_hwnd,
        win32con.WM_COMMAND,
        (win32con.CBN_SELCHANGE << 16) | ctrl_id,
        combo_hwnd,
    )


def focus_window(hwnd):
    """
    Define uma janela como ativa (focada) restaurando-a, colocando-a em primeiro plano e
    aguardando um curto período para que a transição seja efetivada.

    Args:
        hwnd (int): Handle da janela que deverá receber o foco.

    Returns:
        int: O handle da mesma janela, caso seja encontrada; caso contrário, imprime mensagem de erro.
    """
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.2)
    else:
        print("Janela não encontrada!")
    return hwnd
