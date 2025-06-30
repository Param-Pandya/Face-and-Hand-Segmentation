import gradio as gr
from detect_mediapipe import detect_face_hands
from sam2_infer import call_sam2
from visualize import overlay_masks

def run_pipeline(image):
    path = "input/uploaded.jpg"
    image.save(path)
    boxes = detect_face_hands(path)
    mask_urls = call_sam2(path, boxes)
    overlay_masks(path, mask_urls)
    return "sample_outputs/result.png"

gr.Interface(fn=run_pipeline, inputs="image", outputs="image", title="Face & Hand Segmentation with SAM2").launch()
