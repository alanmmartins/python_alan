import pyautogui
import time 

pyautogui.alert("o codigo vai começar.nao use esse computador enquano esse cdigo estiver rodando")
pyautogui.PAUSE =0.5
#abrir o google no eu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(4)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#entrar na area de trabalho
pyautogui.hotkey('winleft','d')
#click p fazer backup e arrastar 
pyautogui.moveTo(1485,130)
pyautogui.mouseDown()
pyautogui.moveTo(1465,756)

#enquanto arasto altero a janela para o google drive
pyautogui.hotkey('alt','tab')
time.sleep(1)
#solta o arquivo no google drive
pyautogui.mouseUp()

#esperar 5 seg
time.sleep(5)

pyautogui.alert('o codigo parou de rodar pode usar seu computador dnv')