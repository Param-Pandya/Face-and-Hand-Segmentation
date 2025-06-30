import cv2
import numpy as np
from matplotlib import pyplot as plt
import requests
from PIL import Image

def overlay_masks(image_path, mask_urls):
    base = cv2.imread(image_path)
    base = cv2.cvtColor(base, cv2.COLOR_BGR2RGB)

    for url in mask_urls:
        response = requests.get(url, stream=True).raw
        mask = Image.open(response).convert("L").resize((base.shape[1], base.shape[0]))
        mask = np.array(mask)
        color_mask = np.zeros_like(base)
        color_mask[:, :, 1] = mask  
        base = cv2.addWeighted(base, 1.0, color_mask, 0.5, 0)

    plt.imshow(base)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("sample_outputs/result.png")
    plt.show()
