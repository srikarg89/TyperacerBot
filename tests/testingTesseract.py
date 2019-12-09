import pyautogui
import time
import numpy
import cv2
import pytesseract
from PIL import Image

time.sleep(1)


typeImg = pyautogui.locateOnScreen('../images/captchaType.PNG',confidence=0.95)
submitImg = pyautogui.locateOnScreen('../images/captchaSubmit.PNG',confidence=0.95)
left = typeImg.left + 8
right = submitImg.left + submitImg.width - 15
top = typeImg.top + typeImg.height + 15
bottom = submitImg.top - 135
image = numpy.array(pyautogui.screenshot(region=(left, top, right - left, bottom - top)))
#image = cv2.imread("../images/testChallenge.PNG")

#image = cv2.imread("images/testChallenge.PNG")
#cv2.imshow("image",image)
#cv2.waitKey(4000)
#cv2.destroyAllWindows()
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
gray = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
#cv2.imshow("thresh",thresh)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()
cv2.imwrite("CaptchaThresh.PNG",thresh)

text = pytesseract.image_to_string(Image.fromarray(thresh), lang='eng')
print(text)
print(len(text))
text = text.replace("\n"," ")
arr = []
text.replace("  "," ")
for index in range(len(text)):
    i = text[index]
    if i == "," or i == ".":
        if index + 2 >= len(text):
            arr.append(".")
        elif ord(text[index+2]) >= 65 and ord(text[index+2]) <= 0:
            arr.append(".")
        else:
            arr.append(",")
    if i == "|" or i == "[" or i == "]":
        arr.append("I")
    else:
        arr.append(i)

print(text)
pyautogui.press([*text])
#string = []
#count = 1
#for i in arr:
#    string.append(i)
#    if count % 5 == 0:
#        pyautogui.press(string)
#        string = []
#    count += 1
#pyautogui.press(string)
