def binarysearch(list1,item):
 low=0
 high=len(list1) - 1
 while low <= high:
     # Finding the Mid of the array
   mid = ( low + high) // 2
     # Mid Element of array
   guess=list1[mid]
   if guess == item:
         # If Item Found at mid Position:
    return mid
   elif guess < item:
       # If Item is greater than Mid position item:
     low=mid+1
   else:
       # If Item is Less than Mid Position Item
       high=mid + 1

 return 0
list1 = [1, 2, 3, 4, 5] # Array Initialisation
print('The elements is found at position',binarysearch(list1,3))
print('The elements is found at position',binarysearch(list1,5))






