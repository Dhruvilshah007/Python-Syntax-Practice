class pycharm:
	def execute(self):
		print("compiling")
		print("Running")
class myeditor:
	def execute(self):
		print("spell check")
		print("convention check")
		print("compiling")
		print("Running")

class laptop:
	def code(self,ide):
		ide.execute()
ide=myeditor()
lap1=laptop()
lap1.code(ide)
		