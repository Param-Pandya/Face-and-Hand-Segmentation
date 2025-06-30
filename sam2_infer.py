import replicate
import os
from dotenv import load_dotenv

load_dotenv()

def call_sam2(image_path, boxes):
    replicate_client = replicate.Client(
    api_token=os.getenv("REPLICATE_API_TOKEN"),
    timeout=60  
    )

    model = replicate_client.models.get("lucataco/segment-anything-2")
    version = model.versions.list()[0]

    prompt_boxes = [{"type": "box", "box": [int(x) for x in b]} for b in boxes]

    with open(image_path, "rb") as f:
        output = replicate_client.run(
            version,
            input={
                "image": f,
                "input_boxes": prompt_boxes
            }
        )

    return output["masks"]
