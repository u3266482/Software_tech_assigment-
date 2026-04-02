# Install NumPy
# pip install numpy

import numpy as np

# ----- Creating Arrays -----

# At the heart of data science and computational analysis 
# lies the fundamental concept of 'representation'. In its essence, 
# representation is the process of encoding and modeling complex, often 
# intangible phenomena using structured and comprehensible formats. 
# Consider the vast and continuous world of sound around us. 
# It's everywhere, yet elusive and transient. 
# We can capture, or more precisely, 
# represent this sound as a series of discrete values in a 1D array. 
# This transformation from the abstract to the tangible is powerful. 
# It allows us to manipulate, analyze, and even recreate the original phenomenon.
# This is just one example, but representation permeates throughout the realm of data. 
# From visualizing galaxies far away based on light waves to predicting future trends using historical data,
# our ability to understand and influence the world hinges on how accurately and effectively we represent it.
# In this NumPy course, we delve deep into the tools and techniques to handle such representations,
# enabling us to harness the true potential of data.

# Why arrays?
# In many computing problems, especially in data science and numerical simulations, we work with large datasets.
# Using standard Python lists to process this data can be inefficient and slow.
# Enter NumPy's arrays, a high-performance alternative built specifically for numerical operations.

# 1D array:
# A 1D array, often called a vector, represents a single list of items.
# Imagine you have the scores of a student in different subjects - that can be represented using a 1D array.
# Another type of data that could be represented as a 1D array is a sound wave (amplitude).
one_dim_array = np.array([1, 2, 3, 4])
print("1D array:", one_dim_array)

# 2D array:
# A 2D array, often referred to as a matrix, is essentially a table or a grid of values.
# Think of this as representing pixel values of a grayscale image, or the scores of multiple students across different subjects.
two_dim_array = np.array([[1, 2], [3, 4], [5, 6]])
print("\n2D array:\n", two_dim_array)

# 3D array:
# When we move to 3D arrays, visualization becomes a bit challenging.
# However, one can think of 3D arrays as a stack of matrices.
# This might be used, for instance, to represent multiple frames of a video or a stack of 2D images.
three_dim_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D array:\n", three_dim_array)


# In summary, understanding the creation of arrays and their types is foundational in numpy.
# It allows for structured data representation, optimized memory usage, and serves as a starting point for more complex operations.


# ----- Array Attributes -----

# After understanding the creation of arrays, it's imperative to dive deeper into the intrinsic properties of these arrays.
# By understanding these attributes, we can gain insights about our data, 
# ensure we are working with the correct data structures, and streamline our data processing tasks.

# Shape of an Array:
# The 'shape' attribute gives us a tuple representing the dimensions of the array.
# For a 1D array, it provides the length of the array. For 2D, it offers the number of rows and columns, and so forth.
print("Shape of 1D array:", one_dim_array.shape)  
print("Shape of 2D array:", two_dim_array.shape)
print("Shape of 3D array:", three_dim_array.shape)

# Think of a classroom seating arrangement. If we were to represent each seat with a number (maybe student ID),
# the shape would tell us how many rows of desks and how many desks per row there are in the classroom.
classroom_seats = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Classroom seating shape (rows x desks):", classroom_seats.shape)

# Dimension of an Array:
# The 'ndim' attribute tells us how many dimensions an array has.
# This is especially useful for a quick check to understand the complexity of our data structure.
print("\nDimension of 1D array:", one_dim_array.ndim)
print("Dimension of 2D array:", two_dim_array.ndim)
print("Dimension of 3D array:", three_dim_array.ndim)

single_book = np.array([1, 2, 3])  # 3 pages
book_shelf = np.array([[1, 2, 3], [4, 5, 6]])  # 2 books, each with 3 pages
entire_bookshelf = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 2 shelves, 2 books on each shelf, 2 pages per book
print("\nDimension of a single book:", single_book.ndim)
print("Dimension of a book shelf:", book_shelf.ndim)
print("Dimension of an entire bookshelf:", entire_bookshelf.ndim)

# Data Type of Elements:
# 'dtype' shows the type of data stored in the array. 
# This can be vital when performing operations on the array or when deciding the type of operations permissible on the array.
print("\nData type of 1D array:", one_dim_array.dtype)

# Size of an Array:
# The 'size' attribute returns the total number of elements in the array.
# It's a quick way to ascertain the volume of data we're dealing with.
print("\nTotal elements in 1D array:", one_dim_array.size)
print("Total elements in 2D array:", two_dim_array.size)

# For a 2D example, think of a chessboard. The total number of squares can be found using size.
chessboard = np.zeros((8, 8))
print("Total squares on a chessboard:", chessboard.size)

# To emphasize the difference between arrays of varying dimensions:
# 1D arrays can be visualized as a single line of values - like a real-world ruler.
# 2D arrays can be thought of as a sheet of values - like a page in a book.
# 3D arrays, on the other hand, add depth. Imagine stacking multiple pages on top of each other, each page having its own grid of values.

# Arrays with specific values:
# In many situations, you might need to start with an array of default values. 
# For instance, initializing a buffer, setting up a "blank canvas", or when performance optimization requires pre-allocation of memory.

# np.zeros gives us an array of just zeros - think of it as a blank slate to which you can then add your data.
zeros_array = np.zeros((2, 2))  
print("\nZeros array:\n", zeros_array)

# np.ones, as the name suggests, provides an array filled with ones.
# This might be useful in cases like image processing where a canvas of white pixels is needed.
ones_array = np.ones((3, 2))  
print("\nOnes array:\n", ones_array)

# arange function:
# Sometimes, you need sequences of numbers in an array format.
# The np.arange function is perfect for this - it's like Python's built-in range but outputs a NumPy array.
# This is especially useful for generating data points for plotting graphs or initializing iterative processes.
range_array = np.arange(10)  
print("\nRange array:", range_array)


# ----- Array Indexing and Slicing -----

# Indexing and slicing are two of the most fundamental operations in data processing.
# They allow us to access or modify specific sections of the data.
# In this section, we explore how to use these operations on NumPy arrays.

# Indexing:
# Indexing is the process of accessing a specific element in an array.
# This is similar to how we access elements in a Python list.
# The syntax for indexing is array[index].
# The index is specified inside the square brackets.
# The index can be a single integer or a tuple of integers.
# A single integer implies the index of the element in the flattened array.
# A tuple of integers implies the indices corresponding to each dimension.

# 1D
one_d = np.array([0, 1, 2, 3, 4, 5])
# Indexing
print(one_d[2])  # Prints 2
print(one_d[-1])  # Prints the last element: 5

# Slicing:
# Slicing is the process of accessing a subset of elements in an array.
# This is similar to how we access a sublist in a Python list.
# The syntax for slicing is array[start:stop:step].
# The start index is inclusive and the stop index is exclusive.
# The step specifies the increment between indices.
# If any of these are not specified, they default to the beginning, end, and 1 respectively.
# Slicing can also be done with a tuple of slices for each dimension.
print(one_d[1:4])  # Prints [1, 2, 3]
print(one_d[::2])  # Prints every second element: [0, 2, 4]

# Practical example for 1D:
# Let's say we have a sound wave sampled at certain intervals. We might want to access or modify specific samples.
sound_wave = np.array([0.5, 0.7, 0.2, 0.4, 0.6])
print("\nOriginal sound wave:", sound_wave)
# Manipulating the third sample
sound_wave[2] = 0.3
print("Modified sound wave:", sound_wave)

# 2D
two_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Indexing
print(two_d[1, 2])  # Prints 6
# Row slice
print(two_d[1])  # Prints second row: [4, 5, 6]
# Column slice
print(two_d[:, 1])  # Prints second column: [2, 5, 8]
# Sub-matrix slice
print(two_d[0:2, 0:2])  # Prints [[1, 2], [4, 5]]

# Practical example for 2D:
# Let's assume we have data of light intensity measured across different wavelengths and at different times.
light_intensity = np.array([[5.2, 5.8, 5.5], [5.0, 5.7, 5.3], [5.1, 5.6, 5.4]])
# Accessing intensity data for the second wavelength at all measured times
second_wavelength = light_intensity[:, 1]
print("\nLight intensities for the second wavelength:", second_wavelength)

# 3D
three_d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
# Indexing
print(three_d[1, 0, 1])  # Prints 6
# Slicing a matrix from 3D array
print(three_d[1])  # Prints second matrix: [[5, 6], [7, 8]]
# Slicing a row from matrices in 3D array
print(three_d[:, 1])  # Prints second row from each matrix: [[3, 4], [7, 8], [11, 12]]
# Slicing a column from matrices in 3D array
print(three_d[:, :, 0])  # Prints first column from each matrix: [[1, 3], [5, 7], [9, 11]]
# Slicing with steps
print(three_d[::2, ::2])  # Takes every second matrix and every second row from each matrix

# Practical example for 3D:
# Consider a situation where we have data about the Earth's temperature over years, at different latitudes, and during different months.
# (This is a simplified example.)
temps = np.array([
    [[15, 20, 18], [16, 21, 19]],  # Year 1
    [[16, 21, 19], [17, 22, 20]],  # Year 2
    [[17, 22, 20], [18, 23, 21]]   # Year 3
])
# Extracting temperature data for the second latitude over all years during the first month.
second_latitude_first_month = temps[:, 1, 0]
print("\nTemperatures for the second latitude during the first month across years:", second_latitude_first_month)



# ----- Array Operations -----

# In NumPy, arrays enable a broad spectrum of operations. These operations can be 
# elemental, where each element in an array undergoes a specific operation, or more complex
# ones that involve entire arrays. Let's dive into these essential concepts.

# Basic Mathematical Operations:
# Just like standard math operations in Python, NumPy arrays support addition, subtraction, 
# multiplication, division, etc., performed element-wise.

# Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Prints [5, 7, 9]

# Multiplication
print(a * 2)  # Multiplies each element by 2, yielding [2, 4, 6]

# Broadcasting:
# NumPy has a powerful feature known as broadcasting. This allows us to perform operations
# on arrays of different shapes, provided certain rules are met. It essentially 'broadcasts'
# the smaller array over the larger one.

matrix = np.array([[1, 2], [3, 4], [5, 6]])
vector = np.array([0.5, 2.5])
print(matrix * vector)  # Multiplies each row of the matrix by the vector

# Universal Functions (ufuncs):
# These are functions that operate element-wise on an array. They are a core feature of NumPy 
# and provide a way to perform fast operations without the need for loops.

# Element-wise square root
print(np.sqrt(a))  # Prints the square root of each element in array 'a'

# Element-wise exponentiation
print(np.exp(a))  # Exponential of each element in array 'a'

# Practical Application:
# Suppose we are tracking tree growth in three different forest regions. 
# Each region has received a different volume of rainfall over three months. 
# We want to see the potential height increase of trees in each region based on the rainfall they received. 
# We have average growth factors for trees per millimeter of rainfall.

# Growth factor for trees per mm of rainfall:
# [Tree Type A, Tree Type B, Tree Type C]
growth_factors = np.array([0.5, 0.3, 0.4])  # in cm/mm

# Rainfall received over three months in three regions:
# Rows: [Region X, Region Y, Region Z]
# Columns: [Month 1, Month 2, Month 3]
rainfall = np.array([[50, 45, 60],   # Region X
                    [30, 35, 25],   # Region Y
                    [40, 40, 50]])  # Region Z

# Calculate the potential height increase for each tree type in each region based on rainfall
# We add a new axis to growth_factors to make it compatible for broadcasting with rainfall.
height_increase = growth_factors[:, np.newaxis] * rainfall

print("Potential height increase in cm:")
print("Region X:", height_increase[0])
print("Region Y:", height_increase[1])
print("Region Z:", height_increase[2])

