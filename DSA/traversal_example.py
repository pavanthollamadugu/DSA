from array import array

arr1= array.array('i',[1,2,4,5,6])
arr2 = array.array('d',[1.4,5.6,4.6])

def travseralarray(n):
    for i in n:
        print(i)
travseralarray(arr1)


