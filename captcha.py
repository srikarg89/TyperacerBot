import time
import numpy as np
import pyautogui
import pytesseract
import cv2
from PIL import Image
from helpers import isolate_by_color, isolate_by_range, threshold_image, get_cluster_idxs, output_text
from scipy.ndimage import label

# Determined using https://imagecolorpicker.com/
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
LOWER_BOUND_BLUE = (150, 150, 0)
UPPER_BOUND_BLUE = (240, 240, 256)

DELAY = 2
time.sleep(DELAY)

# image = Image.open("captchaExample.PNG")
image = pyautogui.screenshot()
image.save("Test.PNG")
image = np.array(image)
image = isolate_by_color(image, WHITE_COLOR)
image = isolate_by_range(image, LOWER_BOUND_BLUE, UPPER_BOUND_BLUE)

captcha_line_idxs = get_cluster_idxs(image, BLACK_COLOR, all_clusters=True, threshold=70)
thresh = threshold_image(image, False, 160)
image[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1]] = [0, 0, 255]
thresh[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1]] = 255
thresh2 = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(thresh), cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)))
thresh2 = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(thresh2), cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8)))
# thresh3 = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(thresh2), cv2.MORPH_DILATE, np.ones((2, 2), np.uint8)))

# whitelist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
# config = f"-c tessedit_char_whitelist='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.#-:/ '"
text = pytesseract.image_to_string(Image.fromarray(thresh2), lang='eng', config='-c tessedit_char_blacklist={0123456789: --psm 6')
print(text)
output_text(text)

# cv2.imshow("thresh", thresh)
# cv2.imshow("thresh2", thresh2)
# cv2.imshow("thresh3", thresh3)
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = pyautogui.screenshot()
# img.save("captchaExample.PNG")

# img = Image.open("captchaExample.PNG")
# img = isolate_text((255, 255, 255))
# img.save("temp.PNG")
