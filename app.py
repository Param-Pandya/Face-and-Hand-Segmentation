import gradio as gr
from detect_yolo_cvlib import detect_face_hands
from sam2_infer import call_sam2
from visualize import overlay_masks
import PIL.Image

def run_pipeline(image: PIL.Image.Image):
    path = "WIN_20250630_18_52_44_Pro.jpg"
    image.save(path)

    boxes = detect_face_hands(path)
    print("Detected Boxes:", boxes)

    mask_urls = call_sam2(path, boxes)
    print("Received Mask URLs:", mask_urls)

    overlay_masks(path, mask_urls)
    return "sample_outputs/result.png"

gr.Interface(
    fn=run_pipeline,
    inputs="image",
    outputs="image",
    title="Face & Hand Segmentation with SAM2"
).launch()
