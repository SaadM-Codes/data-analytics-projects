# QUESTION: 1 (Advanced tasks )
# Importing the NumPy library  
import numpy as np

# creating a 15x15 matrix filled with random integers from 0 to 99
matrix = np.random.randint(100, size=(15, 15))

# Saving the generated matrix to a text file named "matrix.txt"
# - The values are separated by commas (CSV format)
# - fmt="%d" ensures that the numbers are saved as integers without decimals
np.savetxt("matrix.txt", matrix, delimiter=",", fmt="%d")


# AI Used for writing clear and understandable code comments
# Promt used : write comments for making client understanding easy 
# Model : chatGPT