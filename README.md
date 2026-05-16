# 📄 Smart Document Scanner

![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)

A lightweight Computer Vision pipeline that transforms raw, skewed photos of physical documents into clean, flat, top-down scans. Built natively using Python and OpenCV.

---

## ✨ Features

- **Automated Contour Detection**: Automatically detects the borders of a physical document inside a noisy image using edge detection and morphing.
- **Perspective Transformation**: Mathematically corrects the skew and angle of the camera to flatten the image (`four_point_transform`).
- **Image Enhancement**: Converts the image to grayscale and applies light Gaussian smoothing for a clean, professional "scanned" look.
- **Visual Pipeline Logging**: Uses Matplotlib to step through and display each phase of the computer vision process (Grayscale -> Blur -> Canny Edges -> Detected Boundaries).

---

## 🛠️ The Computer Vision Pipeline

1. **Pre-processing**: The image is down-scaled for stability, converted to grayscale, and blurred to remove high-frequency noise.
2. **Edge Detection**: Applies the Canny edge detector to find sharp intensity gradients.
3. **Morphological Operations**: Dilates and closes gaps in the edges to ensure the document boundary is continuous.
4. **Contour Extraction**: Finds the largest quadrilateral contour, assuming it represents the document.
5. **Warp Perspective**: Calculates a transformation matrix and warps the original image into a perfect rectangle.
6. **Post-processing**: Outputs a clean, grayscale `.jpg` ready for sharing.

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have Python 3 installed. Clone the repository and navigate into the folder:

```bash
git clone https://github.com/ananyarajwansh/smart-document-scanner.git
cd smart-document-scanner
```

### 2. Install Dependencies

Install the required computer vision libraries:

```bash
pip install -r requirements.txt
```

### 3. Usage

1. Place the photo of your document inside the project folder.
2. Rename the image exactly to `doc.jpg`. *(Make sure the document edges are clearly visible against the background!)*
3. Run the script:

```bash
python main.py
```

The script will open several matplotlib windows showing the step-by-step transformation. Close the windows to proceed. The final flattened document will be saved in your folder as `scanned_output.jpg`.

---

## 🔮 Future Improvements

- Add direct PDF export using `fpdf2`
- Support multiple document detection in a single image
- Add Optical Character Recognition (OCR) integration using `tesseract`
- Implement dynamic command-line arguments for custom image inputs

---

## 👨‍💻 Author

**Ananya Raj Wansh**
*B.Tech CSE (AI & ML), VIT Bhopal*
- [GitHub](https://github.com/ananyarajwansh)
- [LinkedIn](https://www.linkedin.com/in/ananya-raj-wansh-758689293/)
