#(4,1)and (2,2)
class Simplex:
    def __init__(s,sd):
        s.sd=sd
        s.row=0
        s.column=0
        s.cal()
    def showMatrix(s):
        for i in s.sd:
            for j in i:
                print(j,end=" ")
            print("\n")
    def getone(s):
        for i in range(len(s.sd[0])):
            if s.sd[s.row][s.column]!=1:
                pe=s.sd[s.row][s.column] #pe=pivot element
                for j in range(len(s.sd[0])):
                    s.sd[s.row][j]=s.sd[s.row][j]/pe
    def getzero(s,k):
        for i in range(len(s.sd[0])):
            if s.sd[k][s.column]!=0:
                re=s.sd[k][s.column] #re=remaning element
                for j in range(len(s.sd[0])):
                    s.sd[k][j]=s.sd[k][j]-(s.sd[s.row][j]*re)
    def cal(s):
        while True:
            s.row=int(input("Enter the  Pivot Row: "))
            s.column=int(input("Enter the Pivot Column: "))
            s.row-=1
            s.column-=1
            s.getone()
            a=[]
            for i in range(len(s.sd)):
                a.append(i)
            a.remove(s.row)
            for k in a:
                s.getzero(k)
            s.showMatrix()
            

sd = [
    [-10,-8,0,0,0,0],
    [2,2,1,0,0,140],
    [1,2,0,1,0,120],
    [3,1,0,0,1,150]
    
]
a=Simplex(sd)


 
        
##getone(3,0)
##getzero(3,2,0)
##getzero(3,1,0)
##getzero(3,0,0)
##getone(1,1)
##getzero(1,0,1)
##getzero(1,2,1)
##getzero(1,3,1)
##showMatrix()
