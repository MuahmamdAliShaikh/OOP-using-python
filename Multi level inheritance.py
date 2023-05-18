class Polygon:
    def __init__(s,no_of_sides):
        s.no_of_sides=no_of_sides
        s.sides=[]
    def Take_sides(s):
        for i in range(s.no_of_sides):
            i=float(input("Enter Side " +str(i+1)+" : "))
            s.sides.append(i)
    def Display_sides(s):
        for i in range(s.no_of_sides):
            print("Side "+str(i+1)+" is ",s.sides[i])
class Triangle(Polygon):
    def __init__(s):
        Polygon.__init__(s,3)
    def Find_area(s):
        a,b,c=s.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("The Area of the Triangle is ",area)
class Quadrilateral(Triangle):
    def __init__(s):
        Polygon.__init__(s,4)
    def Take_sides(s):
        for i in range(s.no_of_sides):
            i=float(input("Enter Side " +str(i+1)+" : "))
            s.sides.append(i)
    def Display_sides(s):
        for i in range(s.no_of_sides):
            print("Side "+str(i+1)+" is ",s.sides[i])
    def Find_area(s):
        a,b,c,d=s.sides
        s=(a+b+c+d)/2
        area=((s-a)*(s-b)*(s-c)*(s-d))**0.5
        print("The Area of the Quadrilateral is ",area)

t=Triangle()
t.Take_sides()
t.Display_sides()
t.Find_area()

t=Quadrilateral()
t.Take_sides()
t.Display_sides()
t.Find_area()

