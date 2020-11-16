f=open('file.txt','r')



f1=open('abc.txt','w')

for i in f:
	f1.write(i)



r=open('img.JPG','rb')
f2=open('img2.JPG','wb')

for i in r:
	f2.write(i)