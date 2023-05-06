import numpy as np;

list =[1,2,3]
a1=np.array(list)
print(a1)

print(type (a1)) 
print(a1.shape) #dimension
print(a1.itemsize) #bte size of the array element
print(a1.dtype)  #data type of the elemet in array

a2=np.arange(5)  #creating arrays with numeric range
a3=np.arange(1,10,2,np.float64) #adding datatype 
print(a2,a3)

a4=np.linspace(2.5,5,6) # [2.5 3.  3.5 4.  4.5 5. ] - creating array to get evenly spaced range
print(a4)
