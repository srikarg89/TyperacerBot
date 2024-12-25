import time
import numpy as np
import pyautogui
import pytesseract
import cv2
from PIL import Image
from helpers import isolate_by_color, isolate_by_range, threshold_image, get_cluster_idxs, output_text, clean_text

# Determined using https://imagecolorpicker.com/
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
LOWER_BOUND_BLUE = (150, 150, 0)
UPPER_BOUND_BLUE = (240, 240, 256)

DELAY = 2
time.sleep(DELAY)

image = pyautogui.screenshot()
image = np.array(image)
image = isolate_by_color(image, WHITE_COLOR)
image = isolate_by_range(image, LOWER_BOUND_BLUE, UPPER_BOUND_BLUE)

captcha_line_idxs = get_cluster_idxs(image, BLACK_COLOR, all_clusters=True, threshold=70)
thresh = threshold_image(image, False, 160)
image[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1]] = [0, 0, 255]
thresh[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1]] = 255
thresh[captcha_line_idxs[:, 0] + 1, captcha_line_idxs[:, 1]] = 255
thresh[captcha_line_idxs[:, 0] - 1, captcha_line_idxs[:, 1]] = 255
thresh[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1] + 1] = 255
thresh[captcha_line_idxs[:, 0], captcha_line_idxs[:, 1] - 1] = 255

thresh2 = cv2.bitwise_not(cv2.morphologyEx(cv2.bitwise_not(thresh), cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8)))

text = pytesseract.image_to_string(Image.fromarray(thresh2), lang='eng', config='-c tessedit_char_blacklist=0123456789: --psm 6')
text = clean_text(text)
print(text)
output_text(text)
