class A:
	def feature1(self):
		print("f1")
	def feature2(self):
		print("f2")

class B:
	def feature3(self):
		print("f3")
	def feature4(self):
		print("f4")

class C(A,B):
	def feature5(self):
		print("f5")
	def feature6(self):
		print("f6")


a1=A()				
b1=B()
c1=C()
a1.feature1()
b1.feature2()
c1.feature1()