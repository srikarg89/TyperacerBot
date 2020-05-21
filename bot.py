import pyautogui
import time
import numpy
import cv2
import pytesseract
from PIL import Image

letters = [chr(i) for i in range(97,120,1)]
DELAY = 2

time.sleep(DELAY)
pos = []
for p in pyautogui.locateAllOnScreen('images/wpm.PNG',confidence=0.9):
    pos.append(p)
pos = sorted(pos, key=lambda p: p.top)
last = pos[-1]
print(pos)

p = pyautogui.locateOnScreen('images/change_display2.PNG',confidence=0.9)
gop = pyautogui.locateOnScreen('images/leave_race.PNG',confidence=0.9)
print(p)
print(gop)

top = last.top + last.height + 25
bottom = p.top
left = gop.left + 5
right = p.left + p.width
im = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

image = numpy.array(im)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imwrite("output.PNG",thresh)
text = pytesseract.image_to_string(Image.fromarray(thresh), lang='eng')
text = text.replace("\n"," ")
arr = []
print(text)
text = text.replace("  "," ")
text = text.replace("_","")
text = text.replace("|","I")
text = text.replace("[","I")
text = text.replace("]","I")
print(text)
for index in range(len(text)):
    i = text[index]
    if i == "," or i == ".":
        if index + 2 >= len(text): #End of paragraph
            arr.append(".")
        elif ord(text[index+2]) >= 65 and ord(text[index+2]) <= 90:
            arr.append(".")
        else:
            arr.append(",")
    elif i == "|" or i == "[" or i == "]":
        arr.append("I")
    else:
        arr.append(i)

print(arr)
string = []
count = 1
for i in arr:
    string.append(i)
    if count % 6 == 0:
        pyautogui.press(string)
        string = []
    count += 1
pyautogui.press(string)
