class A:
	def __init__(self):
		print("in A")
	def feature1(self):
		print("feature 1-A")
	def feature2(self):
		print("f2")

class B:
	def __init__(self):
		print("in B")
	
	def feature1(self):
		print("feature 1-B")
	
class C(B,A):
	def __init__(self):
		super().__init__()
		print("in C")
	def feat(self):
		super().feature2()
	
	

a1=C()
a1.feat()