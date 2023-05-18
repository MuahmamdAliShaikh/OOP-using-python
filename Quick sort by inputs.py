class Sort:
    def quick_sort(arr,left,right):
        if left<right:
            partition_pos=Sort.partition(arr,left,right)
            Sort.quick_sort(arr,left,partition_pos-1)
            Sort.quick_sort(arr,partition_pos+1,right)
    def partition(arr,left,right):
        i=left 
        j=right 
        pivot=arr[right]
        while i < j:
            if i<right and arr[i]<pivot:
                i+=1
            elif j>left and arr[j]>=pivot:
                j-=1
            elif i<j:
                arr[i],arr[j]=arr[j],arr[i]
        if arr[i]>pivot:
            arr[i],arr[right]=arr[right],arr[i]
        return i
    def take_inputs():
        cgpa=[]
        fname=[]
        sno=[]
        st=int(input("How many students present in your class? "))
        for i in range(st):
            a=input("Enter Name: ")
            b=int(input("Enter S.NO: "))
            c=float(input("Enter CGPA: "))
            cgpa.append(c)
            fname.append(a)
            sno.append(b)
            arr=list(zip(cgpa,fname,sno))
        Sort.quick_sort(arr,0,len(arr)-1)
        for i in arr:
            print(*i)

Sort.take_inputs()

