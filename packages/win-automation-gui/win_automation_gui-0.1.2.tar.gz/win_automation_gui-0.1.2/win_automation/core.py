import win32gui
import win32con
import time

def find_window(window_name, max_attempts=3, wait_time=2):
    """
    Tenta localizar uma janela pelo nome até um número máximo de tentativas, 
    com um intervalo de tempo entre as tentativas.

    Args:
        window_name (str): Nome da janela que se deseja localizar.
        max_attempts (int): Número máximo de tentativas (padrão: 3).
        wait_time (float): Tempo de espera entre as tentativas, em segundos (padrão: 2).

    Returns:
        int: Handle da janela encontrada.
        None: Se a janela não for encontrada após todas as tentativas.

    Raises:
        Exception: Se a janela não for encontrada após o número máximo de tentativas.
    """
    for attempt in range(max_attempts):
        handle = win32gui.FindWindow(None, window_name)
        if handle != 0:  # Se o handle for diferente de 0, a janela foi encontrada
            print(f"Janela encontrada na tentativa {attempt + 1}: Handle = {hex(handle)}")
            return handle

        print(f"Tentativa {attempt + 1} falhou. Aguardando {wait_time} segundos...")
        time.sleep(wait_time)

    raise Exception(f"Janela '{window_name}' não encontrada após {max_attempts} tentativas.")

def get_control_handle_hex(parent_handle, auto_id, max_attempts=3, wait_time=2):
    """
    Tenta obter o handle do controle até max_attempts vezes,
    esperando wait_time segundos entre as tentativas.

    Args:
        parent_handle (int): Handle da janela pai
        auto_id (int): ID do controle
        max_attempts (int): Número máximo de tentativas
        wait_time (float): Tempo de espera entre tentativas em segundos

    Returns:
        str ou None: Handle em hexadecimal se encontrado
    """
    for attempt in range(max_attempts):
        control_handle = win32gui.GetDlgItem(parent_handle, auto_id)
        if control_handle != 0:
            return hex(control_handle)

        if attempt < max_attempts - 1:  # Não espera após a última tentativa
            print(f"Tentativa {attempt + 1} falhou. Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

    raise Exception(
        f"Controle com auto_id {auto_id} não encontrado após {max_attempts} tentativas"
    )


def is_valid_window(handle):
    """
    Verifica se o handle é válido
    """
    return win32gui.IsWindow(handle)


def get_handle_from_hex(hex_handle):
    """
    Converte o valor hexadecimal (string ou int) para inteiro.
    """
    try:
        if isinstance(hex_handle, str):
            return int(hex_handle, 16)
        return hex_handle
    except ValueError as e:
        raise ValueError(f"Handle inválido: {hex_handle}. Erro: {e}")


def click_button(hex_handle):
    """
    Simula um clique usando BM_CLICK
    """
    try:
        handle = get_handle_from_hex(hex_handle)
        if not is_valid_window(handle):
            raise Exception("Handle inválido ou janela não existe")
        win32gui.SendMessage(handle, win32con.BM_CLICK, 0, 0)
    except Exception as e:
        raise Exception(f"Erro ao clicar no botão: {e}")


def right_click(hex_handle):
    """
    Simula um clique com botão direito
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
    Envia texto para o controle
    """
    try:
        handle = get_handle_from_hex(hex_handle)
        if not is_valid_window(handle):
            raise Exception("Handle inválido ou janela não existe")
        if not isinstance(text, str):
            text = str(text)
        win32gui.SendMessage(handle, win32con.WM_SETTEXT, 0, text)
    except Exception as e:
        raise Exception(f"Erro ao escrever texto: {e}")


def get_control_properties(parent_handle):
    """
    Lista diversas propriedades importantes de cada controle filho da janela especificada.

    As propriedades coletadas:
        - handle: O handle do controle.
        - auto_id: Identificador único do controle.
        - text: Texto associado ao controle (se houver).
        - class_name: Nome da classe do controle.
        - rect: Tupla (left, top, right, bottom) com a posição e dimensões.
        - style: Estilo do controle (GWL_STYLE).
        - ex_style: Estilos estendidos (GWL_EXSTYLE).
        - visible: Booleano indicando se o controle está visível.
        - enabled: Booleano indicando se o controle está habilitado.
        - parent: Handle da janela pai.

    Args:
        parent_handle (int): Handle da janela que se deseja inspecionar.

    Returns:
        list: Uma lista de dicionários contendo as propriedades dos controles.
    """
    controles = []

    def callback(hwnd):
        try:
            # Coleta as propriedades básicas
            auto_id = win32gui.GetDlgCtrlID(hwnd)
            text = win32gui.GetWindowText(hwnd)
            class_name = win32gui.GetClassName(hwnd)

            # Retorna as coordenadas e dimensões do controle
            rect = win32gui.GetWindowRect(hwnd)  # (left, top, right, bottom)

            # Estilos do controle
            style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
            ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)

            # Estado do controle
            visible = win32gui.IsWindowVisible(hwnd)
            enabled = win32gui.IsWindowEnabled(hwnd)

            # Pai e ID do processo
            parent = win32gui.GetParent(hwnd)

            # Armazena todas as informações coletadas
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
        return True  # Continua a enumeração

    # Enumera todos os controles filhos da janela
    win32gui.EnumChildWindows(parent_handle, callback, None)
    return controles
