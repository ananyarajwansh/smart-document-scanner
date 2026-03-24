# 📄 Smart Document Scanner

A Computer Vision project that detects a document from an image and converts it into a clean, flat, scanned version using OpenCV.

---

#Overview

This project simulates a real-world document scanner (like CamScanner or Adobe Scan). It takes an input image, detects the document boundaries, corrects perspective distortion, and produces a clean, readable output.

---

#Features

* Automatic document detection
* Perspective transformation (removes tilt)
* Clean scanned output
* Works on real-world images

---

#Tech Stack

* Python
* OpenCV
* NumPy
* Matplotlib

---

#How It Works

1. Load input image
2. Convert to grayscale
3. Apply edge detection
4. Detect contours
5. Identify document boundary
6. Apply perspective transform
7. Enhance final scanned output

---

#How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-document-scanner.git
cd smart-document-scanner
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python3 main.py
```

---

#Output

The program displays:

* Original Image
* Detected Page Boundary
* Scanned Document
* Final Enhanced Output

---

#Learning Outcomes

* Image preprocessing techniques
* Edge detection using Canny
* Contour detection
* Perspective transformation
* Real-world application of Computer Vision

---

#Note

For already high-quality images, minimal processing is used to avoid over-enhancement and preserve readability.

---

#Future Improvements

* 📄 Export scanned document as PDF
* 📷 Real-time camera scanning
* 🔍 OCR (Text extraction) integration

---

#Author

**Ananya Rajwansh**
B.Tech CSE (AI & ML), VIT Bhopal
