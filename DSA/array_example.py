
#import numpy as np
#np_array = np.array([1,23,4])
 # print(np_array)
#np_array1 = np.array([])
#print(np_array1)


#my_array1= array.array('i', [1,2,3,4])
#my_array1.insert(0,6)
#print(my_array1)


from array import *

arr1= array('i',[1,2,4,5,6])
arr2 =array('d',[1.4,5.6,4.6])

def travseralarray(n):
    for i in n:
        print(i)
travseralarray(arr1)