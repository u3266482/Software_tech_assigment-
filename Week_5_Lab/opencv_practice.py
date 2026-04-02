
# ----- Why OpenCV? And its relation with NumPy -----
import cv2

# OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.
# It contains over 2500 optimized algorithms that provide a comprehensive set of both classic and state-of-the-art 
# computer vision and machine learning tools. OpenCV has been used widely in real-time applications, robotics, 
# and AI research due to its efficiency and easy-to-use API.

# But how does it relate to NumPy?

# NumPy stands out as a critical tool in the OpenCV library. When OpenCV reads an image, it does so in the form 
# of a NumPy array. This means that all the manipulations you might want to do on the image can directly 
# leverage the power of NumPy. Understanding how OpenCV uses NumPy arrays to represent images allows for 
# efficient manipulation and analysis of pixel values. It also means you can seamlessly integrate 
# image data with other data types and sources when analyzing or processing.

# Let's take a look at how this works in practice.

# Install OpenCV
# pip install opencv-python

# Reading an image from the current directory
image = cv2.imread('image.png')

# Let's check the type of the image variable to confirm it's a NumPy array
print(f"Type of the image: {type(image)}")

# The shape of the image array will give us its dimensions
# For colored images, it will typically be a 3D array: (height, width, channels)
# Where channels represent the color channels, typically Red, Green, and Blue (RGB).
print(f"Shape of the image array: {image.shape}")

# However, OpenCV reads images in Blue, Green, Red (BGR) format, not RGB.
# Let's split the channels to see them individually
blue_channel, green_channel, red_channel = cv2.split(image)

# Displaying the individual channels. They will appear grayscale since each channel is a 2D array, 
# but they represent the intensities of the respective colors.
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

# Close all OpenCV windows when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()


# ----- Basic Image Operations -----

# One of the primary advantages of using OpenCV is its vast array of image processing functions.
# In this section, we'll cover some of the fundamental image operations: resizing, grayscale conversion, 
# and drawing on images. Additionally, we'll dive into accessing and modifying pixel values directly, 
# leveraging the fact that images in OpenCV are just NumPy arrays.

# Read the image
image = cv2.imread('image.png')

# 1. Resizing Images:
# Resizing is essential when we need our images to be of a certain size.
# The function `resize()` can be used from OpenCV. The new size is passed as a tuple (width, height).
resized_image = cv2.resize(image, (300, 200))  # resizing to 300x200
cv2.imshow('Resized Image', resized_image)

# 2. Grayscale Conversion:
# Converting an image to grayscale can simplify the image analysis process by removing color information.
# The function `cvtColor()` can be used to convert between various color spaces.
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', grayscale_image)
# How does this change the underlying representation?


# 3. Drawing on Images:
# OpenCV provides several functions to draw shapes and texts on images.
# For example, we can draw a blue rectangle with the function `rectangle()`.
# Parameters: image, top-left corner, bottom-right corner, color (BGR tuple), thickness
cv2.rectangle(image, (50, 50), (200, 100), (255, 0, 0), 2)
# Similarly, we can add text with the function `putText()`.
# Parameters: image, text, bottom-left corner of the text, font, font scale, color, thickness
cv2.putText(image, 'Sample Text', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Drawing on Image', image)

# 4. Accessing and Modifying Pixel Values:
# Given that our image is a NumPy array, accessing and modifying pixel values is straightforward.
# For a colored image, the pixel value itself is an array of Blue, Green, and Red values.
pixel_value = image[100, 100]  # accessing the pixel value at (y=100, x=100)
print(f"Pixel value at (100, 100): {pixel_value}")
# Modifying a pixel value:
image[100, 100] = [0, 0, 255]  # setting the pixel at (y=100, x=100) to red
# Accessing a grayscale pixel value:
gray_pixel_value = grayscale_image[100, 100]
print(f"Grayscale pixel value at (100, 100): {gray_pixel_value}")

# Close all OpenCV windows when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()


# CHALLENGE QUESTION
# Invert the colors of the image by subtracting the pixel values from 255.
# Hint: Use NumPy's array broadcasting feature to subtract 255 from all pixel values at once.

# Invert the pixel values
inverted_image = 255 - image

# Display the original and inverted images side by side
cv2.imshow('Original Image', image)
cv2.imshow('Inverted Image', inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()




# ----- Image Arithmetic with NumPy -----

# Image arithmetic operations allow us to take two (or more) images and combine them in various ways.
# They can be essential for tasks like image blending, creating watermarks, and more.
# One thing to keep in mind is the data type of images. Typically, OpenCV images are 8-bit per channel.
# This means values range from 0 to 255. When performing arithmetic, care must be taken not to "wrap-around" or "clip" values.

# NumPy's Role in Image Arithmetic:
# At its core, OpenCV represents images as multi-dimensional NumPy arrays. Each pixel value in the image is stored as a number 
# (or a set of numbers for colored images) within this array. When we perform arithmetic operations on images using OpenCV functions 
# like cv2.add() or cv2.subtract(), these operations are carried out element-wise on the underlying NumPy arrays. This means that 
# for each pixel (i.e., each number in our NumPy array), the specified arithmetic operation is applied in a highly efficient manner 
# thanks to the optimized operations provided by NumPy. For instance, when we blend two images together using cv2.addWeighted(), 
# OpenCV internally uses NumPy to perform a weighted sum of the pixel values from both images, producing a new image (or NumPy array) 
# as a result. In essence, every time we modify or analyze an image with OpenCV, we are leveraging the power and efficiency of NumPy 
# operations on the underlying data structure. This synergy between OpenCV and NumPy ensures that image processing tasks are both 
# intuitive (due to a consistent data structure) and performant.

# Load two images for demonstration purposes
image1 = cv2.imread('image.png')
image2 = cv2.imread('image2.png')

# Ensure they are the same size for simplicity in this example
# (In practice, you would want to make sure images are the same size before operations)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Adding images
# Direct addition can cause wrapping if values exceed 255.
# It's always a good practice to use cv2.add() which takes care of saturation (i.e., it will cap the value at 255).
added_image = cv2.add(image1, image2)

# Subtracting images
# Similarly, direct subtraction can cause negative values.
# Use cv2.subtract() to handle such cases.
subtracted_image = cv2.subtract(image1, image2)

# Image blending using addWeighted function.
# This function provides an easy way to blend two images. It requires specifying weights for each image.
# blended_image = alpha*image1 + beta*image2 + gamma
# Here, alpha and beta are the weights, and gamma is an added scalar (usually kept as 0).
alpha = 0.7
beta = 0.3
gamma = 0
blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

# Display results
cv2.imshow("Added Image", added_image)
cv2.imshow("Subtracted Image", subtracted_image)
cv2.imshow("Blended Image", blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# When working with image arithmetic and blending, understanding the underlying NumPy operations is crucial.
# NumPy provides an array-based approach to handle pixel-wise operations, ensuring performance and flexibility.

