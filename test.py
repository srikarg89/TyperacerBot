import pyautogui
import time

time.sleep(1.5)
p = pyautogui.locateOnScreen('images/change_display_format.PNG',confidence=0.97)
print(p)