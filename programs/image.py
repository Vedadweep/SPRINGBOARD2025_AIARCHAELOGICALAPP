import cv2

# Read an image
img = cv2.imread("C:\\Users\\Vedadweep\\OneDrive\\Pictures\\20250620_OBGA.AdobeStock_506819660_bing.jpg")   # replace with your file path

# Check if image loaded successfully
if img is None:
    print("Error: Could not read image.")
else:
    cv2.namedWindow("My Image", cv2.WINDOW_NORMAL)
    # Show the image in a window
    cv2.imshow("My Image", img)

    # Wait until a key is pressed, then close
    cv2.waitKey(0)
    cv2.destroyAllWindows()