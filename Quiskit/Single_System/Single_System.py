import numpy as np #Uses array class from NumPy library to perform matrix and vector computations






#Defines two column vectors corresponding to |0> and |1>
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])
print(ket0/2 + ket1/2) #Prints average of the two column vectors


