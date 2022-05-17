import webbrowser as web
import pyautogui
from time import sleep

print("""\


 __          ___    _       _______ _____         _____  _____    ______ _      ____   ____  _____  ______ _____  
 \ \        / / |  | |   /\|__   __/ ____|  /\   |  __ \|  __ \  |  ____| |    / __ \ / __ \|  __ \|  ____|  __ \ 
  \ \  /\  / /| |__| |  /  \  | | | (___   /  \  | |__) | |__) | | |__  | |   | |  | | |  | | |  | | |__  | |__) |
   \ \/  \/ / |  __  | / /\ \ | |  \___ \ / /\ \ |  ___/|  ___/  |  __| | |   | |  | | |  | | |  | |  __| |  _  / 
    \  /\  /  | |  | |/ ____ \| |  ____) / ____ \| |    | |      | |    | |___| |__| | |__| | |__| | |____| | \ \ 
     \/  \/   |_|  |_/_/    \_\_| |_____/_/    \_\_|    |_|      |_|    |______\____/ \____/|_____/|______|_|  \_\
                                                                                                                  
                                                                                                                  

                    """)

print('Phone number: ')
tlf = input()

print('Message: ')
msg = input()

print('Number of messages: ')
n = int(input())

web.open("https://web.whatsapp.com/send?phone=" + tlf)
sleep(10)

for i in range(n):
    pyautogui.typewrite(msg)
    pyautogui.press('enter')