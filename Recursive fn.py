#Program of recursive function
def fn(a,b):
 if b==0:
     return 1
 elif b<1:
     return 1/a*fn(a,b+1)
 else:
     return a*fn(a,b-1)
    
print(fn(2,-3))

def factorial(n):
    if n==0:
        return 1
    else:
        a=n*factorial(n-1)
        return a
print(factorial(6))

# #Program for Binary Search
# a=[1,2,3,4,5,6,7,8,9,10]
# search_no=int(input("Enter the search element: "))
# i=a[0]
# l=len(a)-1
# def find(i,l,search_no):
#     mid=int((i+l)/2)
#     if a[mid]==search_no:
#         print(f"{search_no} found at index no {mid}")
#     elif a[mid]<search_no:
#         return find(mid+1,l,search_no)
#     elif a[mid]>search_no:
#         return find(i,mid-1,search_no)
# find(i,l,search_no)


#Program of Euclidean for greatest common divisor
##def gcd(a,b):
##    if b>a:
##        (a,b)=(b,a)
##    elif b==0:
##        return a
##    else:
##        return gcd(b,a%b)
##print(gcd(98,56))



