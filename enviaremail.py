import pyautogui
import time 

pyautogui.alert("o codigo vai começar.nao use esse computador enquano esse cdigo estiver rodando")
pyautogui.PAUSE =0.5
#entrar no gmail
pyautogui.hotkey('winleft','r')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(4)
pyautogui.write('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.press('enter')

#enviar posiçoes para tela
pyautogui.moveTo(1014, 174)
pyautogui.mouseDown()
pyautogui.mouseUp()

#pyautogui.moveTo(1477,593)
#pyautogui.mouseDown()
#pyautogui.mouseUp()
#email para quem vc vai enviar
pyautogui.write('alanmunozmartins@gmail.com')
pyautogui.press('enter')
pyautogui.press('tab')
#assunto
pyautogui.write('teste')
pyautogui.press('tab')

pyautogui.write('assunto')

#pyautogui.moveTo(1584,1007)
#pyautogui.mouseDown()
#pyautogui.mouseUp()

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

pyautogui.write('emaill')
pyautogui.press('enter')


pyautogui.hotkey('ctrl-enter')

#pyautogui.moveTo(1496, 1022)
#pyautogui.mouseDown()
#pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('o codigo parou de rodar pode usar seu computador dnv')