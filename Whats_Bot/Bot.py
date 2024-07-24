import pandas as pd
import pyautogui as pag
import time

def iniciar_whatsapp():
    # Abrir o menu Iniciar e pesquisar por WhatsApp
    pag.press('win')
    time.sleep(1)
    pag.write('whatsapp')
    time.sleep(2)
    pag.press('enter')
    time.sleep(5)  # Esperar o WhatsApp abrir completamente

def enviar_mensagem(numero, mensagem):
    try:
        # Clicar na barra de pesquisa do WhatsApp (para digitar o nome do contato)
        pag.click(x=192, y=115)
        time.sleep(2)
        pag.write(numero)
        time.sleep(3)

        # Selecionar o contato encontrado
        pag.click(x=224, y=174)
        time.sleep(2)

        # Clicar na área de digitação de mensagem e enviar a mensagem
        pag.click(x=845, y=1016)
        time.sleep(2)
        pag.write(mensagem)
        time.sleep(2)
        pag.press('enter')
        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

# Caminho para a planilha
caminho_planilha = r'C:\Users\id03041\Documents\Python_Programas\pythonProject\planilhadecontatos\contatos_mensagens.xlsx'

# Ler a planilha, ignorando a primeira linha (cabeçalho)
try:
    planilha = pd.read_excel(caminho_planilha, skiprows=1, header=None)
except Exception as e:
    print(f"Erro ao ler a planilha: {e}")
    exit()

# Abrir o WhatsApp apenas uma vez
iniciar_whatsapp()

# Iterar sobre cada linha da planilha
for _, linha in planilha.iterrows():
    try:
        numero = linha[0]  # Números de telefone na coluna A
        mensagem = linha[1]  # Mensagens na coluna B

        enviar_mensagem(numero, mensagem)
        time.sleep(2)  # Esperar um pouco antes de enviar a próxima mensagem
    except Exception as e:
        print(f"Erro ao processar a linha: {e}")

print('Todas as mensagens foram enviadas com sucesso')
