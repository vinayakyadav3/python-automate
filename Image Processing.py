import cv2
from PIL import Image
import matplotlib.pyplot as plt

# Read and display an image using OpenCV
image = cv2.imread('image.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Open and show an image using PIL
image = Image.open('image.jpg')
image.show()

# Resize an image using PIL
resized_image = image.resize((width, height))
resized_image.show()

# Apply a filter to an image using OpenCV
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
