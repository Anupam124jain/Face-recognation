import cv2
import numpy as np

# texel_coord = uv_coord * [width, height]
img = cv2.imread("/home/rits/Documents/Assets/UAE_identity/EID_New_Formats/eid_new_back3.jpg")
h, w, c = img.shape

# Chip icon
x = round(0.081198275 * w)
y = round(0.27992284 * h)
w = round(0.19849685 * w)
h = round(0.28704292 * h)

crop_img = img[y:y+h, x:x+w]

cv2.imwrite("cropped_chip_icon.jpg", crop_img)
