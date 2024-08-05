import tkinter as tk
from tkinter import messagebox
import pyautogui as pag
import time
from pynput.keyboard import Controller, Key

# Inicializar o controlador de teclado
keyboard = Controller()

def digitar_com_pynput(texto):
    for char in texto:
        if char == '\n':
            keyboard.press(Key.ctrl)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            keyboard.release(Key.ctrl)
        else:
            keyboard.press(char)
            keyboard.release(char)
        time.sleep(0.05)

def iniciar_whatsapp():
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
        pag.click(x=230, y=190)
        time.sleep(2)

        # Clicar na área de digitação de mensagem
        pag.click(x=845, y=1016)
        time.sleep(2)

        # Digitar a mensagem usando pynput para garantir que caracteres especiais sejam digitados corretamente
        digitar_com_pynput(mensagem)
        time.sleep(2)
        pag.press('enter')
        print(f"Mensagem enviada para {numero}")
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")

def enviar():
    nomes = nome_entry.get("1.0", "end-1c").strip().split('\n')
    mensagem = mensagem_entry.get("1.0", "end-1c")

    if not nomes or not mensagem.strip():
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    iniciar_whatsapp()

    for nome in nomes:
        enviar_mensagem(nome, mensagem)
        time.sleep(2)

    messagebox.showinfo("Sucesso", "Todas as mensagens foram enviadas com sucesso.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("WhatsApp Bot")

tk.Label(root, text="Nomes (um por linha):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
nome_entry = tk.Text(root, height=10, width=40)
nome_entry.grid(row=1, column=0, padx=10, pady=10)

tk.Label(root, text="Mensagem:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
mensagem_entry = tk.Text(root, height=10, width=40)
mensagem_entry.grid(row=3, column=0, padx=10, pady=10)

enviar_button = tk.Button(root, text="Enviar Mensagens", command=enviar)
enviar_button.grid(row=4, column=0, padx=10, pady=10)

root.mainloop()
