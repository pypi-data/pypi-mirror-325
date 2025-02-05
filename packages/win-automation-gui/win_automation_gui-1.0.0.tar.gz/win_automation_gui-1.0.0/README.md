# Win Automation

**Win Automation** é uma biblioteca Python para automação de controles GUI no Windows. Utilizando a API Win32 via PyWin32, a biblioteca fornece funções para interagir com janelas e seus controles de forma programática, seja para obter handles, simular cliques, enviar textos ou listar propriedades dos controles.

## Funcionalidades

- **Obter Handle de Controle:**  
  A função `get_control_handle_hex` tenta encontrar o handle de um controle a partir do seu `auto_id`, com múltiplas tentativas configuráveis e intervalos de espera.

- **Simulação de Cliques:**  
  * `click_button` executa um clique simples (usando a mensagem BM_CLICK).  
  * `right_click` simula um clique com o botão direito.

- **Envio de Texto para Controles:**  
  * `write_text` utiliza a mensagem WM_SETTEXT para enviar texto a controles compatíveis.

- **Listagem de Controles:**   
  * `get_control_properties` retorna diversas propriedades de cada controle, como texto, classe, dimensões (retângulo), estilos, visibilidade, entre outros.

## Requisitos

- Python 3.6 ou superior
- [PyWin32](https://github.com/mhammond/pywin32) (instalado automaticamente via pip)

## Instalação

Depois de publicado no PyPI, você pode instalar a biblioteca com:

```bash
pip install win-automation