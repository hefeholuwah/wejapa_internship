import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(start=1,stop=26,step=1).reshape(5,5)
print("integers:",X)

# Use Boolean indexing to pick out only the odd numbers in the array

Y= (X[X%2==1])
print("odd:",Y)
