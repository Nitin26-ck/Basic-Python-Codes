import numpy as np

a=np.array([12,34,5,67,8,90]) 
print('array elements are:',a) 
a2=np.append(a,[30,77])
print('inter array elements are:',a2)
a3=np.insert(a,4,44)
print('intermed array elements are :',a3)
a4=np.delete(a,5)
print('current array elements are',a4)

