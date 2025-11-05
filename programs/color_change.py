import cv2

# Load an image
img = cv2.imread("C:\\Users\\Vedadweep\\OneDrive\\Pictures\\20250620_OBGA.AdobeStock_506819660_bing.jpg")   # Replace with your file path

# Check if image loaded correctly
if img is None:
    print("Error: Could not read image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show both
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original", img.shape[1], img.shape[0])
cv2.imshow("Original", img)

cv2.namedWindow("Grayscale", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Grayscale", img.shape[1], gray.shape[0])
cv2.imshow("Grayscale", gray)

# Wait until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save grayscale image
cv2.imwrite("grayscale_output.jpg", gray)