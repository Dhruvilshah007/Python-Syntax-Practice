def person(name,**data):
	print(name)
	for i,j in data.items():
		print(i,j)


person('navin',age=20,city='malad',mob=9409072451)

