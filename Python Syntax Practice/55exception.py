a=2
b=6


try:
	print("resource open")
	print(a/b)
	k=int(input("enter a number"))
	print(k)
except ZeroDivisionError as e:
	print("you cant divide a number by zero",e)
except ValueError as e:
	print("invalid input")
except Exception as e:
	print("something  went wrong....")
