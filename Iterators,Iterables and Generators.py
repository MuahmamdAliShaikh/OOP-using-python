#Iterable-Object in which __iter or __getitem method defined means it can give iterator
#Iterator-Object in next method define means in which we switch one by one on other elements
#Iteration-kisi bhi cheeze ko iterate karna or iss ka next element ko fetch karna
#Generator-Iterator jo hum sirf aik bar iterate karsakhta means iss sa aik bar value generate kar sakhta hain
##def gen(n): #generator ki waja sa on the fly value generate hoti ha or Ram bhi kam utilize hoti 
##    for i in range(n):
##        yield i
####for i in gen(1000000):
####    print(i)
##obj1=gen(3)
##print(next(obj1))or print(obj1.__next__())
##print(next(obj1))
###print(next(obj1))
##
##list1=[1,2,3,4,5]
##list2=["A","B","C","D","E"]
##print(zip(list1,list2))
##print(list(zip(list1,list2)))
##c=zip(list1,list2)
##for i in c:
##    print(*i) #or print(i[0],i[1])
##c=iter(list1) #or c=list1.__iter__()
##print(next(c))or print(next(c))or print(next(c))or print(next(c))or print(next(c))
##
##d=iter("Hello")
##print(hasattr(d,'__iter__')) or print(hasattr(d,'__next__'))
##s='Hello'
##print(hasattr(s,'__iter__')) or print(hasattr(s,'__next__'))
##
##class avgAdj:
##    def __init__(s,data):
##        s.data=data
##        s.len=len(data)
##        s.first=0
##        s.second=1
##    def __iter__(s):
##        return s
##    def __next__(s):
##        if s.second==s.len:
##            raise StopIteration
##        else:
##            s.avg=(s.data[s.first]+s.data[s.second])/2
##            s.first+=1
##            s.second+=1
##        return s.avg
##a=avgAdj([10,20,30,40,50])
##for i in a:
##    print(i)
##import random
##c=list(random.choice(range(1,10))for _ in range(30))#generator expression
##d=(i**2 for i in c)#generator comprehsion
###print("Output values using generator comprehensions:", end = ' ')
###for var in d:
##	#print(var, end = ' ')
##
##import sys
##lst=[i*i for i in range(4)]
##gen=(i*i for i in range(4))
##print(sys.getsizeof(lst))
##print(sys.getsizeof(gen))
##
def Gen(n):
    for i in range(n+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                yield i

for i in Gen(6):
    print(i)
