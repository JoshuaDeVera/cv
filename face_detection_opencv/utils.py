import cv2

def detect(cascade, gray_image, image):
    detected_objects = cascade.detectMultiScale(gray_image, 2.5, 20)
    for x, y, w, h in detected_objects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)
    return image