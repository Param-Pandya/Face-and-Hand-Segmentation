from detect_yolo_cvlib import detect_face_hands
from sam2_infer import call_sam2
from visualize import overlay_masks

image_path = "input/mannequin.jpg"

boxes = detect_face_hands(image_path)
print("Detected boxes:", boxes)

mask_urls = call_sam2(image_path, boxes)
print("Received mask URLs")

overlay_masks(image_path, mask_urls)
