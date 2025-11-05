import cv2

# Read image
img = cv2.imread("C:\\Users\\Vedadweep\\OneDrive\\Pictures\\20250620_OBGA.AdobeStock_506819660_bing.jpg")

if img is None:
    print("Error: Could not read image.")
else:
    # Flip vertically (0), horizontally (1), or both (-1)
    flip_vertical = cv2.flip(img, 0)
    flip_horizontal = cv2.flip(img, 1)
    flip_both = cv2.flip(img, -1)

    # Show results
    # Show results with resizable windows
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original", img.shape[1], img.shape[0])
    cv2.imshow("Original", img)

    cv2.namedWindow("Flipped Vertically", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Flipped Vertically", flip_vertical.shape[1], flip_vertical.shape[0])
    cv2.imshow("Flipped Vertically", flip_vertical)

    cv2.namedWindow("Flipped Horizontally", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Flipped Horizontally", flip_horizontal.shape[1], flip_horizontal.shape[0])
    cv2.imshow("Flipped Horizontally", flip_horizontal)

    cv2.namedWindow("Flipped Both", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Flipped Both", flip_both.shape[1], flip_both.shape[0])
    cv2.imshow("Flipped Both", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()