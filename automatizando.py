import pyautogui
import time

email= pyautogui.prompt("Please enter your email address")
password= pyautogui.password("Please enter your password")

pyautogui.PAUSE = 0.5
pyautogui.alert("o codgo vai começar nao mexa o seu computador")

with pyautogui.hold("win"):
    pyautogui.press("r")
    
pyautogui.write("chrome -incognito")
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.write("https://drive.google.com/drive/my-drive")    

pyautogui.press("enter")
time.sleep(3)

for i in range(0,9):
    pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(3)


pyautogui.write(email)
pyautogui.press("enter")
time.sleep(4) 
pyautogui.write(password)
pyautogui.press("enter")

#localizacao do aerquivo
arquivo_path = r"C:\Users\Aluno\python_alan\destino"

time.sleep(5) 
pyautogui.hotkey("shift","u")
pyautogui.write(arquivo_path)
pyautogui.press("enter")  