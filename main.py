import cv2
import matplotlib.pyplot as plt
import numpy as np

def show(title, img, gray=False):
    plt.figure(figsize=(8, 10))
    if gray:
        plt.imshow(img, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")
    plt.show()

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]   # top-left
    rect[2] = pts[np.argmax(s)]   # bottom-right

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]   # top-right
    rect[3] = pts[np.argmax(diff)]   # bottom-left

    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

# Load image
image = cv2.imread("doc.jpg")
if image is None:
    print("Error: Image not found")
    exit()

orig = image.copy()
show("Original Image", image)

# Resize for stable contour detection
ratio = image.shape[0] / 800.0
new_height = 800
new_width = int(image.shape[1] / ratio)
image = cv2.resize(image, (new_width, new_height))

# Preprocess
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

show("Grayscale", gray, gray=True)
show("Blur", blur, gray=True)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Strengthen page boundary
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
edges = cv2.dilate(edges, kernel, iterations=2)
edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=3)

show("Edges", edges, gray=True)

# Find contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

print("Number of contours found:", len(contours))

if len(contours) == 0:
    print("Could not detect the page.")
    exit()

# Take the largest contour
largest_contour = contours[0]

# Create a rotated rectangle around the page
rect = cv2.minAreaRect(largest_contour)
box = cv2.boxPoints(rect)
page_contour = np.array(box, dtype="float32")

# Draw detected page boundary
detected = image.copy()
cv2.drawContours(detected, [page_contour.astype(int)], -1, (0, 255, 0), 3)
show("Detected Page Boundary", detected)

# Scale contour back to original image size
page_contour = page_contour.reshape(4, 2) * ratio

# Perspective transform
scanned = four_point_transform(orig, page_contour)
show("Scanned Document", scanned)

# Final clean output (minimal processing)
scanned_gray = cv2.cvtColor(scanned, cv2.COLOR_BGR2GRAY)

# Very light smoothing (optional)
final_scan = cv2.GaussianBlur(scanned_gray, (3, 3), 0)

show("Final Scanned Output", final_scan, gray=True)
cv2.imwrite("scanned_output.jpg", final_scan)