import numpy as np
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(1,10).reshape(3,3)

print(arr1,arr2)

#Addition of Two Numpy Array
addTwoArray=arr1+arr2
print(addTwoArray)

#Multiply of Two Numpy Array
multiplyTwoArray=arr1 * arr2
print(multiplyTwoArray)

#Divide of Two Numpy Array

divideTwoArray=arr1 / arr2
print(divideTwoArray)


#Substract of Two Numpy Array

SubstractTwoArray=arr1 - arr2
print(SubstractTwoArray)

#Matrix Product of Two NumPy Array (matrix)
#using @ operator and .dot() operator

matrixProduct=arr1 @ arr2
print(matrixProduct)

matrixProductDot=arr1.dot(arr2)
print(matrixProductDot)



#NumPy Mathematical Built-in functions
'''
1.np.max()
2.np.argmax()
3.np.min()
4.np.argmin()
5.np.sum()
6.np.mean()
7.np.sqrt()
8.np.std()
9.no.exp()
10.no.log()
11.np.log10()
'''
# 1.np.max()
print(arr1.max())
print(arr1.max(axis=0))
print(arr1.max(axis=1))

#2.np.argmax()
print(arr1.argmax())

#3.np.min()
print(arr1.min())

#4.np.argmin()
print(arr1.argmin())

#5.np.sum()
print(arr1.sum())
print(arr1.sum(axis=1))

# 6.np.mean()
print(arr1.mean())

#7.np.sqrt()
Sqrt=np.sqrt(arr1)
print(Sqrt)

# 8.np.std()
standardDivision=np.std(arr2)
print(standardDivision)

# 9.no.exp()
exponentialValue=np.exp(arr2)
print(exponentialValue)
# 10.no.log()
naturalLog=np.log(arr2)
print(naturalLog)
# 11.np.log10()
base10=np.log10(arr1)
print(base10)


