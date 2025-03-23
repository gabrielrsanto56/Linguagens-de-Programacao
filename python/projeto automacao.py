import pyautogui
import time

def chatpgt():
    pergunta_chat = input("faça uma pergunta ao chatgpt: ")
    pyautogui.press("win")
    pyautogui.write("brave")
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.write("chatgpt.com")
    pyautogui.press("enter")
    largura, altura = pyautogui.size()
    x = largura/2
    y = altura/2
    pyautogui.moveTo(x, y, duration=1.3)
    pyautogui.click
    pyautogui.write(pergunta_chat)
    pyautogui.press("enter")

def youtube():
    pyautogui.press("win")
    pyautogui.write("brave")
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.write("youtube.com")
    pyautogui.press("enter")

def whatsapp():
    contato = input("para qual contato deseja enviar a mensagem? ")
    mensagem = input("digite a mensagem para o contato ")
    pyautogui.press("win")
    pyautogui.write("whatsapp")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(contato)
    pyautogui.press("tab")
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.write(mensagem)
    pyautogui.press("enter")


acao = int(input("""o que deseja fazer? 
                 [0] SAIR 
                 [1] FAZER PERGUNTA AO CHATGPT
                 [2] ACESSAR O YOUTUBE
                 [3] MANDAR UMA MENSAGEM NO WHATSAPP 
                 """))
while acao !=0:
    if acao == 1:
        chatpgt()
    elif acao == 2:
        youtube()
    elif acao == 3:
        whatsapp()
    else:
        print("OPÇÃO INVÁLIDA! ")
    acao = int(input("o que deseja fazer? "))