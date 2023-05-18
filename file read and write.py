#https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/#must visit on this link

f=open("Emp.txt","r+")#read and write
f.read()
f.write("Newline \n")#move file position to the end of the file
f.close()

f=open("Emp.txt","w+") #write and read
f.write("test 1\n")
f.write("test 2\n")
f.write("test 3\n") #now the file pointer is at the end
f.seek(0) ## move the file pointer to the beginning
print(f.read())

f=open("Emp.txt","a+")
f.seek(0) #file pointer at end, move to beginning
lines=f.readlines()
print(len(lines))

f=open("Emp.txt","a")#test 4 print in the end and not create file from beginnig
f.write("test 4")
f.close()

f=open("Emp.txt","r")
print(f.read())
f.readlines())
f.close()
