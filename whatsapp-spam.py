import webbrowser as web
import pyautogui
from time import sleep

web.open("https://web.whatsapp.com/send?phone=+34673295331")
sleep(10)

with open("message", "r") as file:
    for i in range(500):
        pyautogui.typewrite("4,9 suspenso")
        pyautogui.press("enter")