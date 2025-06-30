# Face-and-Hand-Segmentation


### ✅ Download Instructions

Since you're unable to download directly, here's what you can do:

#### Option 1: **Copy-Paste Manually**

1. **Create a new file** named `README.md` in your project folder.
2. **Copy and paste** the following content into it:


```markdown
# 🧠 Face & Hand Segmentation using SAM2

This project performs **automated face and hand segmentation** in images using a combination of **YOLO + cvlib** for detection and **SAM2** (Segment Anything Model 2 via Replicate API) for fine-grained segmentation. A **Gradio web UI** is also included for quick testing.

> **🔧 Created by Param Pandya**  
> **🐍 Requires: Python 3.10**

---

## 📦 Features

- Detects **faces** using `cvlib` (OpenCV + DNN backend)
- Detects **hands** using **YOLOv8**
- Sends bounding boxes to **SAM2** (via Replicate API)
- Overlays the segmentation masks on the original image
- Includes **CLI** and **Web UI** (via Gradio)
- Fully automated — no manual input required

---

## 📁 Project Structure

```plaintext
.
├── app.py                  # Gradio UI
├── main.py                 # CLI pipeline
├── detect_yolo_cvlib.py    # Face & hand detection
├── sam2_infer.py           # Calls SAM2 API (Replicate)
├── visualize.py            # Overlays masks on the image
├── requirements.txt        # Python dependencies
├── input/                  # Input image directory
├── sample_outputs/         # Output images with segmentation
└── .env                    # Your API key (not committed)
```

---

## 🔧 Setup

### ✅ Prerequisites

- Python 3.10
- Replicate API Key: Get one from https://replicate.com/account/api-tokens

### 🛠 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/face-hand-segmentation-sam2.git
cd face-hand-segmentation-sam2

# Create virtual environment (recommended)
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
````

### 🔐 Configure API Key

Create a `.env` file in the root folder:

```
REPLICATE_API_TOKEN=your_replicate_api_token
```

---

## 🚀 Usage

### 1. Command-Line Interface (CLI)

Process an image via the command line:

```bash
python main.py
```

> ✏️ Make sure to place your test image in `input/` and update the filename in `main.py`.

### 2. Gradio Web UI

Launch an interactive browser app:

```bash
python app.py
```

Upload an image and view segmented output instantly.

---

## 🧠 How It Works

1. **Detection**
   Uses `cvlib` for **face detection** and **YOLOv8** (via `ultralytics`) for **hand detection**.

2. **Segmentation (SAM2)**
   The bounding boxes are sent to Replicate's **SAM2 model**, which returns segmentation masks.

3. **Visualization**
   The masks are downloaded and overlaid on the original image using OpenCV and Matplotlib.

---

## ⚠️ Known Limitations

* 🧤 Hand detection might miss occluded or partially visible hands.
* 👥 Works best for images with 1–2 subjects; batch processing not yet optimized.
* 🌐 Performance depends on network/API response from Replicate.

---

## ✅ Requirements

See `requirements.txt` or install via:

```bash
pip install -r requirements.txt
```

Main libraries used:

* `cvlib`, `opencv-python`
* `ultralytics` (YOLOv8)
* `replicate`, `python-dotenv`
* `matplotlib`, `gradio`

---

## 👤 Author

**Param Pandya**
📎 [GitHub](https://github.com/param-pandya)
💼 [LinkedIn](https://www.linkedin.com/in/param-pandya)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE) – free to use and modify.

