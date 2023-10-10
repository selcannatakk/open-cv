import cv2 as cv
import os
import numpy as np

image = cv.imread(os.path.join('.', 'data', 'image.jpeg'))
resize_image = cv.resize(image, (640, 480))

image_edge = cv.Canny(resize_image, 100, 200)

image_edge_d = cv.dilate(image_edge, np.ones((5, 5), dtype=np.int8))

image_edge_e = cv.erode(image_edge, np.ones((1, 1), dtype=np.int8))


cv.imshow('image', image_edge_e)
cv.waitKey(0)
