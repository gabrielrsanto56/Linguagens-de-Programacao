import pyautogui #biblioteca para fazer as automações
import time #biblioteca de tempo 

pyautogui.press("win") #pressiona o botão do windows
pyautogui.write("brave") #escreve o que se deseja procurar (no meu caso o navegador brave)
pyautogui.press("enter") #pressiona o botão enter
time.sleep(1) #espera um segundo. É necessário porque as vezes o computador pode atrasar na hora de digitar a url
pyautogui.write("https://github.com/gabrielrsanto56") #faz com que o automador digite uma url
pyautogui.press("enter")
