import cv2 as cv
import numpy as np


def get_limits(color):

    c = np.uint8([[color]])
    hsv_color = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    lower_limit = hsv_color[0][0][0] - 10, 100, 100
    upper_limit = hsv_color[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return lower_limit, upper_limit
