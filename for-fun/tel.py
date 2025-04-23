import pyautogui
import time

time.sleep(4)  
for _ in range(1000):  
    pyautogui.write('mahdi', interval=0.01)  
    pyautogui.press('enter')  

