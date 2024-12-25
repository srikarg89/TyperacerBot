import time
import cv2
import numpy as np
import pyautogui
from scipy.ndimage import label

# PyAutoGUI functions
def isolate_by_color(image, color, threshold=0):
    # Isolate the text region.
    lower_bound = [color[0] - threshold, color[1] - threshold, color[2] - threshold]
    upper_bound = [color[0] + threshold, color[1] + threshold, color[2] + threshold]
    return isolate_by_range(image, lower_bound, upper_bound)


# image is an np array
def isolate_by_range(image, lower_bound, upper_bound):
    # Isolate the text region.
    mask = np.bitwise_and(np.all(image >= lower_bound, axis=-1), np.all(image <= upper_bound, axis=-1))

    # Remove points that aren't near any other points (outliers).
    labeled_mask, num_features = label(mask)
    sizes = {i: np.sum(labeled_mask == i) for i in range(1, num_features + 1)}
    maxkey = max(sizes, key=sizes.get)
    boundary_idxs = np.argwhere(labeled_mask == maxkey).astype(np.int32)

    left, top, right, bottom = boundary_idxs[:, 0].min(), boundary_idxs[:, 1].min(), boundary_idxs[:, 0].max(), boundary_idxs[:, 1].max()
    left, top, right, bottom = int(left), int(top), int(right), int(bottom)
    return image[left:right, top:bottom]


def get_cluster_idxs(image, color, all_clusters, threshold=0):
    lower_bound = [color[0] - threshold, color[1] - threshold, color[2] - threshold]
    upper_bound = [color[0] + threshold, color[1] + threshold, color[2] + threshold]
    return get_cluster_idxs_by_range(image, lower_bound, upper_bound, all_clusters)


def get_cluster_idxs_by_range(image, lower_bound, upper_bound, all_clusters):
    mask = np.bitwise_and(np.all(image >= lower_bound, axis=-1), np.all(image <= upper_bound, axis=-1))
    if all_clusters:
        return np.argwhere(mask).astype(np.int32)

    # Remove points that aren't near any other points (outliers).
    labeled_mask, num_features = label(mask)
    sizes = {i: np.sum(labeled_mask == i) for i in range(1, num_features + 1)}
    maxkey = max(sizes, key=sizes.get)
    return np.argwhere(labeled_mask == maxkey).astype(np.int32)


def output_text(arr, speed = None):
    string = []
    count = 1
    for i in arr:
        string.append(i)
        if count % 6 == 0:
            pyautogui.press(string)
            if speed is not None:
                # assume 6 characters = 1.5 words
                # 1.5 words * 60 / delay = speed (wpm)
                # delay = 90 / speed
                time.sleep(50 / speed)
            string = []
        count += 1
    pyautogui.press(string)

# OpenCV functions

def threshold_image(image, blur, threshold_val=200):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if blur:
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(gray, threshold_val, 255, cv2.THRESH_BINARY)
    return thresh

def clean_text(text):
    # Common mistakes in OCR
    text = text.replace("\n"," ")
    text = text.replace("  "," ")
    text = text.replace("_","")
    text = text.replace("|","I")
    text = text.replace("[","I")
    text = text.replace("]","I")
    text = text.replace("}","I")
    text = text.replace("{","I")

    # Following a period, the next letter should be capitalized.
    updated_text = ""
    for index in range(len(text)):
        i = text[index]
        if i == "," or i == ".":
            # The paragraph never ends in a comma.
            if index + 2 >= len(text):
                updated_text += "."
            elif (ord(text[index+2]) >= 65 and ord(text[index+2]) <= 90) or (ord(text[index+3]) >= 65 and ord(text[index+3]) <= 90):
                updated_text += "."
            else:
                updated_text += ","
        else:
            updated_text += i
    return updated_text
