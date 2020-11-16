a=10
def something():
	global a
	a=15
	print("in function",a)
something()
print("outside function",a)



a=10
print(id(a))

def something():
	a=9
	x=globals()['a']
	print(id(x))
	print("in function",a)
	globals()['a']=15
something()
print(a)


