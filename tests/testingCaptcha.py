import pyautogui
import time
import numpy
import numpy as np
import cv2
import pytesseract
from PIL import Image

letters = [chr(i) for i in range(97,120,1)]

"""
time.sleep(2)
pos = []
for p in pyautogui.locateAllOnScreen('images/wpm.PNG',confidence=0.95):
    pos.append(p)
#    print(p)
num = 0
while num < len(pos):
    box = pos[num]
    for num2 in range(len(pos) - num - 1):
        box2 = pos[num2+1]
        #Get rid of overlapping boxes (probably the same thing)
        if not (box.left > box2.left + box2.width or box2.left > box.left + box.width or box2.top > box.top + box.height or box.top > box2.top + box2.height):
            pos.remove(box)
            num -= 1
            break
    num += 1
#print(pos)
p = pyautogui.locateOnScreen('images/change_display_format.PNG',confidence=0.97)
#pos.append(p)
gop = pyautogui.locateOnScreen('images/blue_arrow.PNG',confidence=0.97)
#print(p)
#pos3 = pos[len(pos)-1]
pos1 = pos[len(pos)-1]
print(gop,pos1,p)
top = gop.top
bottom = p.top
left = gop.left + gop.width
right = p.left + p.width
im = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
#print(pos3.top - pos1.top - pos1.height)
"""

image = cv2.imread("images/testChallenge.PNG")
for row in range(len(image)):
    for col in range(len(image[row])):
        pixel = image[row][col]
        works = True
        for a in pixel:
            if a > 80:
                works = False
        if works:
            image[row][col] = numpy.array([255,255,255])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
_,cnts,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for c in cnts:
    rect = cv2.boundingRect(c)
    cv2.contourArea(c)
    x, y, w, h = rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("image",image)
key = cv2.waitKey(0)
if key == 27:
    print('hi')
cv2.destroyAllWindows()
"""
text = pytesseract.image_to_string(Image.fromarray(thresh), lang='eng')
text = text.replace("\n"," ")
arr = []
for i in text:
    if i == "|":
        arr.append("I")
    else:
        arr.append(i)

text.replace("  "," ")
print(text)
"""
"""
string = []
count = 1
for i in arr:
    string.append(i)
    if count % 5 == 0:
        pyautogui.press(string)
        string = []
    count += 1
pyautogui.press(string)
"""