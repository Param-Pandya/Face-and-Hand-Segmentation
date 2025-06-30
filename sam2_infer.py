import replicate
import os
from dotenv import load_dotenv
load_dotenv()

def call_sam2(image_path, boxes):
    replicate_client = replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))
    model = replicate.models.get("meta/sam2")
    version = model.versions.get("latest")

    prompt_boxes = [{"type": "box", "box": b} for b in boxes]

    with open(image_path, "rb") as f:
        output = version.predict(image=f, input_boxes=prompt_boxes)

    return output["masks"]
