import os
from urllib import request
conn=request.urlopen("http://www.el.com/")
b=conn.read()
wp=b.decode("cp1252")
ep=0
p=wp.find("<a",ep+1)
f=open("D:\\Webscraping\\Data.txt","w")
while p>=0:
    sp=wp.find("\"",p)+1
    ep=wp.find("\"",sp)
    f.write("\n")
    f.write(wp[sp:ep])
    p=wp.find("<a",ep+1)




#These are the extra codes for list of the file by using os
#fd = os.open("D:\\Webscraping\\Data.txt", os.O_RDONLY)
#fileobj = os.fdopen(fd)
#lines = fileobj.readlines()
#lines = [line.strip() for line in lines]
#print(lines)

