import struct
##f=open("int.bin","wb")
##a=4096
##f.write(str(a).encode())
##b=struct.pack("i",a)
##c=struct.unpack("i",b)
##f.write(str(b).encode())
##f.close()
##print(b)
##print(c*2)
##print(c[0]*2)
##print(c[0])
##f=open("int.bin","rb")
##a=f.read(4)
##b=struct.unpack("i",a)#i-format C-type is int and takes 4 bytes
##c=struct.unpack("f",a)#f-format C-type is float and takes 4 bytes
##print(a)
##print(b[0],c[0]) #[0] is only used to remove tuple

##f=open("all_gray.bmp","rb")
##s1=f.read(1)
##s2=f.read(1)
##s3=f.read(2)
##print(s1,s2,s3)
##a=f.read(4)
##filesize=struct.unpack("i",a)
##print(filesize)

f=open("all_gray.bmp","rb")
f.seek(18,0)
w=f.read(4)
h=f.read(4)
width=struct.unpack("i",w)
height=struct.unpack("i",h)
print("Width of Image=",width[0],"Height of Image=",height[0])


