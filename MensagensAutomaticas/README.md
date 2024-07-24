# 📱 WhatsApp Automation Bot

## 📖 Descrição
Este projeto é um bot que automatiza o envio de mensagens para colaboradores da empresa via WhatsApp Desktop. O bot lê uma planilha com números de telefone e respectivas mensagens, procura o número na lista de contatos do WhatsApp e envia a mensagem.

## ⚙️ Funcionalidades
- 🚀 Envio automatizado de mensagens via WhatsApp Desktop.
- 📊 Leitura de planilha com números de telefone e mensagens dos colaboradores.
- 🖥️ Abertura automática do WhatsApp Desktop.

## 👍 Pontos Positivos
- 🤖 Automatiza a tarefa repetitiva de envio de mensagens para vários contatos.
- ⏱️ Reduz o tempo e esforço manual necessário para enviar mensagens individualmente.
- 🛠️ Fácil de configurar e usar em uma máquina.

## ❌ Contras
- 💻 O programa é feito para usar em uma máquina específica devido aos parâmetros de x e y da tela.
- 📋 A planilha precisa ser formatada corretamente, com os números de telefone na primeira coluna e as mensagens na segunda.
- 📏 As coordenadas da tela podem variar em diferentes resoluções e tamanhos de tela, o que pode causar falhas na execução em outras máquinas.
- ❓ Não há verificação se a mensagem foi realmente entregue.

## 📋 Requisitos
- 🐍 Python 3.x
- 📦 Bibliotecas: `pyautogui`, `pandas`, `openpyxl`
