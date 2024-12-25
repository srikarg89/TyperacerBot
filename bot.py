import time
import pyautogui
import pytesseract
import numpy as np
from helpers import isolate_by_color, output_text, threshold_image, clean_text
from PIL import Image

# Determined using https://imagecolorpicker.com/
TEXT_BOUNDARY_COLOR = (246,251,255)

DELAY = 2
time.sleep(DELAY)

image = pyautogui.screenshot()
image = isolate_by_color(np.array(image), TEXT_BOUNDARY_COLOR)

# Crop the image to only include text region.
text_mask = np.argwhere(np.max(image, axis=-1) < 10)
image = image[text_mask[:, 0].min() - 10:text_mask[:, 0].max() + 10, text_mask[:, 1].min() - 10:text_mask[:, 1].max() + 10]
thresh = threshold_image(image, False)

# Show the result
text = pytesseract.image_to_string(Image.fromarray(thresh), lang='eng')
text = clean_text(text)
print(text)
output_text(text)
