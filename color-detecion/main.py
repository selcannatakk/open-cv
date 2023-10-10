import cv2 as cv


from PIL import Image
from utils import get_limits

yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv.VideoCapture(0)
while True:

    ret, frame = cap.read()

    hsv_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)

    mask = cv.inRange(hsv_image, lower_limit, upper_limit)
    mask = Image.fromarray(mask)

    bbox = mask.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)

    cv.imshow('frame', mask)

    print(bbox)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
