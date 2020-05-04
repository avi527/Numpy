import numpy as np

#How to create one dimensional NumPy array?
oneDArray=np.array([1,2,3,4,5,6])
print(oneDArray)
#check dimenssion
print(oneDArray.ndim)
#How to check the size of the NumPy array?
print("size",oneDArray.size)
#How to check the shape
print(oneDArray.shape,"shape")
print(type(oneDArray))
#How to the data type of NumPy ndarray?
print(oneDArray.dtype,'dtype')

#How to create Two dimensional NumPy array?
twoDArray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDArray)
#check dimenssion
print("size",twoDArray.size)
#How to check the shape
print(twoDArray.shape,"shape")
print(twoDArray.ndim)
#How to check the size of the NumPy array?
print(type(twoDArray))
#How to the data type of NumPy ndarray?
print(twoDArray.dtype,'dtype')



############################Create metrics using python NumPy functions ############################
'''Ones metrics use NumPy ones() function.'''
'''
----------------------SYNTEX----------------------
1.np.ones(shape, dtype=None, order=‘C’)
2.np.zeros(shape, dtype=None, order=‘C’)
3.np.empty(shape, dtype=None, order=‘C’)

#Create NumPy 1D array using arange() function

4.Syntax: np.arange([start,] stop[, step,], dtype=None)

#Create NumPy 1D array using linspace() function

5.np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0,)

#Convert 1D array to multidimensional array using reshape() function

6. np.reshape(a, newshape, order=‘C’)

#Convert multidimensional array in one dimensional

7.np.ravel(array_name, order=‘C’)  or  array_name.ravel(order=‘C’)
 array_name.flatten(order=‘C’)

 #Transpose metrics

8.np.transpose(array_name, axes=None)  or array_name.T'''

###############SLUTIONS#########################SOLUTIONS##################################

#1
npOnes=np.ones([4,3],dtype=int)
print(npOnes)

#2
npZeros=np.zeros([3,3],dtype=int)
print(npZeros)

#3
'''By default NumPy empty() function give float64 bit random value. According to your requirement change dtype.'''
npEmpty=np.empty((2,4))
print(npEmpty)

#4
arr=np.arange(4,20)
print(arr)

#5
npLinespace=np.linspace(2,3,4)
print(npLinespace)

#6
arr=[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
arr_reshape = np.reshape(arr, (3,4))
print(arr_reshape)

#7
array=arr_reshape.flatten()
print(array)

#8
arr=array.transpose()
print(arr)

