#Program of Quick Sort
def quicksort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        quicksort(arr,left,partition_pos-1) #for j work
        quicksort(arr,partition_pos+1,right) #for i work

def partition(arr,left,right):
    i=left #0 index
    j=right #7 index
    pivot=arr[right] #44
    while i < j:
        if i<right and arr[i]<=pivot:
            i+=1
        elif j>left and arr[j]>=pivot:
            j-=1
        elif i<j:
            #print(arr[i],arr[j])
            arr[i],arr[j]=arr[j],arr[i]
            #print(arr[i],arr[j])
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i

arr=[50,11,88,66,55,77,33,44]
quicksort(arr,0,len(arr)-1)
print(arr)

