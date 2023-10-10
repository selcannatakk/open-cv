import cv2 as cv
import mediapipe as mp
import os


def process_img(image, face_detection):
    img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            # cv.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 10)
            # blur faces
            image = cv.blur(image[y1:y1 + h, x1:x1 + w, :], (10, 10))

    return image


output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# read image
image_path = './data/image.jpeg'

image = cv.imread(image_path)
image = cv.resize(image, (640, 480))

H, W, _ = image.shape

# detect faces
face_detection = mp.solutions.face_detection

with face_detection.FaceDetetction(model_selection=0, min_detection_confidence=0.5) as face_detection:
    image = process_img(image, face_detection)
    # cv.imshow('image',image)
    # cv.waitKey(0)

# save image
cv.imwrite(os.path.join(output_dir, 'output.png'), image)
