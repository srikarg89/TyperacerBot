import pyautogui
import time
import numpy
import cv2
import pytesseract
from PIL import Image

letters = [chr(i) for i in range(97,120,1)]

time.sleep(2)
pos = []
for p in pyautogui.locateAllOnScreen('images/wpm.PNG',confidence=0.95):
    pos.append(p)
print(pos)
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
#pos1 = pos[len(pos)-1]
#print(gop,pos1,p)
top = gop.top
bottom = p.top
left = gop.left + gop.width
right = p.left + p.width
im = pyautogui.screenshot(region=(left, top, right - left, bottom - top))
#print(pos3.top - pos1.top - pos1.height)
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
    if count % 4 == 0:
        pyautogui.press(string)
        string = []
    count += 1
pyautogui.press(string)
