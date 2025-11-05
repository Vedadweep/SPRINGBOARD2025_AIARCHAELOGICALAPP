import cv2

# Load an image
img = cv2.imread("C:\\Users\\Vedadweep\\OneDrive\\Pictures\\20250620_OBGA.AdobeStock_506819660_bing.jpg")   # Replace with your file path

# Check if the image loaded correctly
if img is None:
    print("Error: Could not read image.")
    exit()

# Resize image (width=300, height=300)
resized = cv2.resize(img, (300, 300))

# Show both
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", img.shape[1], img.shape[0])
cv2.imshow("Original", img)

cv2.namedWindow("Resized", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resized", resized.shape[1], resized.shape[0])
cv2.imshow("Resized", resized)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the resized image
cv2.imwrite("resized_output.jpg", resized)