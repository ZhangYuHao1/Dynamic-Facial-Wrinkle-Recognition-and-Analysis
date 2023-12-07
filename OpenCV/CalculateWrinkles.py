import cv2
import numpy as np

# Load the image
image = cv2.imread('test.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred, 10, 50)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area or other criteria if needed
# contours = [contour for contour in contours if cv2.contourArea(contour) > threshold_area]

# Calculate the length of each contour
for contour in contours:
    arc_length = cv2.arcLength(contour, True)
    print("Wrinkle length:", arc_length)

    # Draw the contour and its length on the image
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    cv2.putText(image, f"Length: {arc_length:.2f}", (contour[0][0][0], contour[0][0][1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image with contours and lengths
cv2.imshow('Wrinkle Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
