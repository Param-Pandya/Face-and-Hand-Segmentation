import cv2
import cvlib as cv
from ultralytics import YOLO

def detect_faces(image_path):
    image = cv2.imread(image_path)
    faces, _ = cv.detect_face(image)
    return faces 

def detect_hands(image_path):
    model = YOLO("yolov8n.pt") 
    results = model(image_path)
    boxes = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id].lower()
            if "hand" in class_name: 
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append([x1, y1, x2, y2])
    return boxes

def detect_face_hands(image_path):
    face_boxes = detect_faces(image_path)
    hand_boxes = detect_hands(image_path)
    return face_boxes + hand_boxes
