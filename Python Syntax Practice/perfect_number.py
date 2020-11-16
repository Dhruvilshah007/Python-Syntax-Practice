#perfect number




n=int(input("enter the value of n"))
ans=0
prod=1

while (n!=0):
	r=n%10
	prod=prod*int(r)
	ans=ans+int(r)
	prod=prod*int(r)
	n=n/10


print(prod)
print(ans)


if (ans==prod):
	print("its an Perfect number")
else:
	print("NOt perfect number")