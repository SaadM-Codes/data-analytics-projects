# QUESTION: 1 (Advanced tasks )
# Importing the NumPy library 
import numpy as np

# Loading the matrix from the "matrix.txt" file
# - delimiter="," ensures that values are correctly separated (CSV format)
# - dtype=np.int32 ensures that the values are read as 32-bit integers
reading_matrix = np.loadtxt("matrix.txt", delimiter=",", dtype=np.int32)

# Printing the loaded matrix to verify its contents
print(reading_matrix)


# # AI Used for writing clear and understandable code comments
# Promt used : wirte comments for making client understanding easy 
# Model : chatGPT