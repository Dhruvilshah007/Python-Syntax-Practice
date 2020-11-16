lst=[10,19,20,34,65,7,0]

def count(lst):
	even=0
	odd=0
	for i in lst:
		if i%2==0:
			even+=1
		else:
			odd+=1
	return even,odd

even,odd=count(lst)
print("no. of even is",even)
print("no. of odd is",odd)
