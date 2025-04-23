import pyautogui
import time

time.sleep(4)  
for _ in range(1000):  
    pyautogui.write('maman', interval=0.1)  
    pyautogui.press('enter')  
    time.sleep(1)   
