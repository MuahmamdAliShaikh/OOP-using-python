a=[0,1,1,0,0,0,1,0,1,0,1,1,1,1,0]
a.insert(0," ")
n=1
for i in range(len(a)):
    if 2**i<(len(a)+i+1):
        a.insert(2**i,"h"+str(n))
        n+=1
print("DATA AFTER INSERT BITS: ",a[1:])

def ham(n):
    h=[]
    for i in range(2**(n-1),len(a),2**n):
        for j in range(i,i+2**(n-1)):
            if j<len(a):
                h.append(a[j])
    print(h)
    d=h[1:]
    if sum(d)%2!=0:
        a[2**(n-1)]=1
        
    else:
        a[2**(n-1)]=0

for i in range(len(a)):
    if 2**i<(len(a)+i+1):
        ham(i+1)
print("TRANSMITTED DATA BITS: ",a[1:])

s=[0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
print("RECEVIED DATA BITS: ",s)
s.insert(0," ")
def check(n):
    h=[]
    for i in range(2**(n-1),len(s),2**n):
        for j in range(i,i+2**(n-1)):
            if j<len(s):
                h.append(s[j])
    if sum(h)%2!=0:
        s[2**(n-1)]=1
        
    else:
        s[2**(n-1)]=0


for i in range(len(s)):
    if 2**i<(len(s)+i+1):
        check(i+1)

c=[]   
for i in range(len(s)):
    if 2**i<(len(s)+i+1):
        c.append(s[2**i])

count=0
for i in range(len(c)):
    a=c[i]*2**i
    count+=a
if count==0:
    print("NO ERROR FOUND")
else:
    print("ERROR FOUND AT",count,"POSITION")
    

###Code for h1 
##for i in range(1,len(a),2):
##    for j in range(i,i+1):
##        if j<len(a):
##            print(a[j])
##    print()
##
###Code for h2
##for i in range(2,len(a),4):
##    for j in range(i,i+2):
##        if j<len(a):
##            print(a[j])
##        print()
##
###Code for h3
##for i in range(4,len(a),8):
##    for j in range(i,i+4):
##        if j<len(a):
##            print(a[j])
##        print()
###Code for h4
##for i in range(8,len(a),16):
##    for j in range(i,i+8):
##        if j<len(a):
##            print(a[j])
##        print()
##
###Code for h5
##for i in range(16,len(a),32):
##    for j in range(i,i+16):
##        if j<len(a):
##            print(a[j])
##        print()
