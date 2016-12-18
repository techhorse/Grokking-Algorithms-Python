
# Function Definition For Finding The smallest number

def findsmallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

# Function Definition For sorting the array
def selectionsort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest=findsmallest(arr)          # Function Call
        newarr.append(arr.pop(smallest))    # New Array addition
    return newarr
print(selectionsort([5,3,6,2,10]))    # Print The Array After sorting
