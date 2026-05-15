
---
 
# 🧠 Face & Hand Segmentation using SAM2

This project performs **automated face and hand segmentation** in images using a combination of **YOLOv8** and **cvlib** for detection, and **SAM2** (Segment Anything Model 2 via Replicate API) for fine-grained segmentation. A **Gradio web UI** is included for interactive testing.

> 🔧 **Created by Param Pandya**
> 🐍 **Python version:** 3.10+

---

## 📦 Features

* ✅ Face detection using `cvlib` (OpenCV + DNN)
* ✅ Hand detection using YOLOv8 (`ultralytics`)
* ✅ Precise segmentation via SAM2 (Replicate API)
* ✅ CLI and web interface (Gradio)
* ✅ Fully automated pipeline (no clicks needed)

---

## 📁 Project Structure

```plaintext
.
├── app.py                  
├── main.py                 
├── detect_yolo_cvlib.py    
├── sam2_infer.py           
├── visualize.py            
├── requirements.txt        
├── input/                  
├── sample_outputs/         
└── .env                    
```

---

## 🔧 Setup Instructions

### ✅ Prerequisites

* Python 3.10
* A Replicate API token (get one from [https://replicate.com/account/api-tokens](https://replicate.com/account/api-tokens))

### 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/face-hand-segmentation-sam2.git
cd face-hand-segmentation-sam2

# (Optional) Create and activate a virtual environment
python3.10 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 🔐 Add Replicate API Key

Create a `.env` file in the project root with the following line:

```
REPLICATE_API_TOKEN=your_replicate_api_token
```

---

## 🚀 Usage

### 1. CLI (Command Line Interface)

To process an image via command line:

```bash
python main.py
```

> ⚠️ Make sure to place your image inside the `input/` folder and update the path in `main.py` accordingly.

---

### 2. Web UI (Gradio)

To launch the interactive web app:

```bash
python app.py
```

* Upload an image.
* The system detects faces and hands.
* SAM2 is used to generate masks.
* A masked result image is returned.

---

## 🧠 How It Works

1. **Detection**

   * Uses `cvlib` for face detection
   * Uses YOLOv8 for hand detection (`ultralytics`)

2. **Segmentation**

   * The detected bounding boxes are sent to the **SAM2** model via Replicate
   * SAM2 returns high-quality mask URLs

3. **Overlay**

   * The masks are downloaded and overlaid on the input image using OpenCV and Matplotlib

---

## ⚠️ Limitations

* 👋 May not be able to detect occluded or partially visible hands
* 👥 Supports multiple faces/hands sequentially, not in batches

---

## ✅ Requirements

To install all required packages:

```bash
pip install -r requirements.txt
```

**Key Libraries:**

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

## 📄 License

This project is licensed under the [MIT License](LICENSE).
Feel free to use, modify, and share.

---


