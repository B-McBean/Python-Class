# Crash Course in Python
# Author: Breanna McBean
# Select functions from the NumPy package
# May 28, 2019

##############################################
# Using the NumPy Package (especially NumPy Arrays)

# importing a package (adding "as np" allows us to shorten what we type in the future)
import numpy as np

# Why use numpy arrays?
# - less memory used
# - faster run-time

# observations
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
print("height:", height)
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
print("weight:", weight)

# creating numpy arrays
# Use "np" to tell Python what package to check for the function
np_height = np.array(height)
print("np_height:", np_height)
np_weight = np.array(weight)
print("np_weight:", np_weight)

# Print the data type of the variable
print("np_height type:", type(np_height))

# Print the type of elements held in the array
print("np_height element type:", np_height.dtype)

# Create a multi-dimensional np array
np_data = np.array([height, weight])
print("np_data:")
print(np_data)

# You can print the dimensions of the data
print("dimensions of np_data:", np_data.shape)

# You can print the number of elements in the array
print("number of elements in np_data:", np_data.size)

# There are also many ways to create an array

# You can create an array and specify the data type of the elements
a = np.array([[1, 2, 4], [5, 8, 7]], dtype='int')
print("creating an np array with lists:", a.dtype)
# Instead of lists, you can also use tuples to create an np array

# Creating a 3X4 array with all zeros
b = np.zeros((3, 4))
print("initializing np array full of zeros:")
print(b)

# You can also choose a number to initialize all of the elements to (if you don't want 0)
c = np.full((3, 3), 6, dtype='complex')
print("initializing np array with a specific value:")
print(c)

# You can also randomize inputs from the distribution of your choice
d = 5 * np.random.random_sample((3, 2))
print("initializing np array from a random sample in [0,5):")
print(d)
# Check out https://docs.scipy.org/doc/numpy/reference/routines.random.html for more information
# on how to sample from different distributions

# Create a sequence of integers from 0 to 30 with steps of 5
e = np.arange(0, 30, 5)
print("creates a np array using arange:", e)
# Like range, this is not inclusive on the second endpoint

# Create a sequence of 10 values in range 0 to 5
f = np.linspace(0, 5, 10)
print("creates np array using linspace:")
print(f)
# This is like the linspace command from MATLAB

# You can reshape arrays. Here, we will reshape 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
# Reshape the array to 3 dimensions
new_arr = arr.reshape(2, 2, 3)
print("original array:")
print(arr)
print("reshaped array:")
print(new_arr)

# You can also flatten numpy arrays
# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
fl_arr = arr.flatten()
print("original array:")
print(arr)
print("flattened array:")
print(fl_arr)

# You can also look at only certain portions of arrays
# Arrange elements from 0 to 19
g = np.arange(20)
print("np array with elements 0-19:", g)

# Here, we are "slicing" the array. The format is arr[start:stop:step]
h = g[8:17:1]
print("creates np array of the 8th-17th element of g:", h)

# Choosing one of the indices as negative starts counting from the end of the array rather than the start
i = g[-8:17:1]
print("creates np array of 8th element from the end of g to the 17th element of g:", i)

# Like in MATLAB, the : operator means all elements till the end.
j = g[10:]
print("creates np array of 10th-last elements of g:", j)

# You can also look at portions of an array which meet a given condition.
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("original array:")
print(arr)
cond = arr > 0
# cond is a boolean array
print("boolean array of which elements in the original array meet the condition:")
print(cond)
temp = arr[cond]
print("flat array of elements that met the condition:")
print(temp)

# You can also perform many operations on arrays
k = np.array([1, 2, 5, 3])
print("original array:", k)

# You can add 1 to every element
print("original array +1:", k+1)

# You can subtract 3 from each element
print("original array -3:", k-3)

# You can multiply each element by 10
print("original array times 10:", k*10)

# You can square each element
print("square each element of the original array:", k**2)

# You can modify existing numpy arrays
k *= 2
print("assigned doubled array to original array:", k)

# You can take the transpose of numpy array
m = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])

print("original array:")
print(m)
print("transpose array:")
print(m.T)

# NumPy arrays also support unary operators
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
print("original array:")
print(arr)

# You can get the maximum element of array
print("max element:", arr.max())
# You can find the maximum element in a row
print("np array of max elements by row:", arr.max(axis=1))
# Choosing axis=0 gives the maximum of each columns

# You can get the minimum element in each column
print("np array of min elements by column", arr.min(axis=0))
# Choosing axis=1 gives minimum of each row

# You can get the sum of array elements
print("sum of each element in the array:", arr.sum())

# You can get the cumulative sum along each row
print("np array of cumulative sum of elements going across each row:")
print(arr.cumsum(axis=1))
# Choosing axis=0 gives teh cumulative sum along each column

# NumPy arrays also support binary operations
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[4, 3],
              [2, 1]])
print("array 1:")
print(a)
print("array 2:")
print(b)
# You can add arrays
print("array 1 + array 2:")
print(a + b)

# You can perform element-wise multiplication
print("element wise multiplicatio of arrays 1 and 2:")
print(a * b)

# You can perform matrix multiplication
print("matrix multiplication of array 1 * array 2:")
print(a.dot(b))

# NumPy also contains many common mathematical functions that can be performed on arrays

# You can perform trig operations
c = np.array([0, np.pi / 2, np.pi])
print("original array:", c)
print("sin of each element:", np.sin(c))

# You can exponentiate array values
d = np.array([0, 1, 2, 3])
print("original array:", d)
print("exponentiate each element:", np.exp(d))

# You can take the square root of array values
print("square root each element:", np.sqrt(d))

# You can also sort arrays. We will sort the following array:
e = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])
print("original array:")
print(e)

# Sort the array (returns a flat array of sorted values
print("flattened sorted array:", np.sort(e, axis=None))

# Sort the array row-wise
print("each row of the array sorted:")
print(np.sort(e, axis=1))
# Choosing axis=0 gives column-wise sorted array

# Note: Adding an extra argument, "kind= 'sort_algo'", you can choose the sorting algorithm.
# If you're familiar with sorting algorithms and have a large array this may be beneficial to you.

# You can also sort an array by certain values

# Fist, set alias names for dtypes
dtypes = [('name', object), ('grad_year', int), ('cgpa', float)]
# np array requires strings to have a fixed length, so use 'object' for the data type and it can store a
# string of any length

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
arr = np.array(values, dtype=dtypes)
print("original array:")
print(arr)

# You can sort the array by name
print("array sorted by name:")
print(np.sort(arr, order='name'))

# You can also sort the array by grad year first then by the cumulative gpa
print("array sorted by grad year then GPA:")
print(np.sort(arr, order=['grad_year', 'cgpa']))

