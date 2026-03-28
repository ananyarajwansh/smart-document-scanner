# Smart Document Scanner

This project is a simple implementation of a document scanner using Computer Vision techniques. The goal is to take an image of a document and convert it into a clean, flat, scanned version.

---

## What the project does

The program reads an input image, detects the boundaries of the document, and then corrects the perspective so that the document looks like it was scanned from the top. The final output is saved as an image.

---

## Tools and Libraries Used

* Python
* OpenCV
* NumPy
* Matplotlib

---

## How to run the project

### 1. Install Python

Make sure Python 3 is installed on your system. You can check using:

```
python3 --version
```

---

### 2. Install required libraries

Open terminal and run:

```
pip3 install -r requirements.txt
```

---

### 3. Add input image

Place your document image inside the project folder and rename it as:

```
doc.jpg
```

Make sure the document is clearly visible in the image.

---

### 4. Run the program

In the terminal, navigate to the project folder and run:

```
python3 main.py
```

---

### 5. Output

After running the program:

* The processed images will be displayed
* The final scanned document will be saved as:

```
scanned_output.jpg
```

---

## How it works (in brief)

* The image is converted to grayscale
* Edges are detected to identify boundaries
* Contours are used to locate the document
* A perspective transform is applied
* The final image is cleaned and saved

---

## Notes

* The results are best when the document is clearly visible and not heavily blurred
* For already clear images, minimal processing is applied to avoid distortion

---

## Future Improvements

* Add PDF export
* Support multiple documents
* Improve detection for complex backgrounds

---

## Author

Ananya Raj Wansh
B.Tech CSE (AI & ML), VIT Bhopal
