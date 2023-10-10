import cv2 as cv
import os

# 1.
image = cv.imread(os.path.join('.', 'data', 'image.jpeg'))
resize_image = cv.resize(image, (640, 480))
gray_image = cv.cvtColor(resize_image, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray_image, 140, 255, cv.THRESH_BINARY)
thresh = cv.blur(thresh, (10, 10))
# 2.
image2 = cv.imread(os.path.join('.', 'data', 'image2.jpeg'))
resize_image2 = cv.resize(image2, (640, 480))
gray_image2 = cv.cvtColor(resize_image2, cv.COLOR_BGR2GRAY)

thresh2 = cv.adaptiveThreshold(gray_image2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 30)
ret2, thresh2 = cv.threshold(gray_image2, 140, 255, cv.THRESH_BINARY)

cv.imshow('image2', thresh2)
cv.waitKey(0)
