#Sum of digits of number

n=int(input("enter the value of n"))

ans=0

while (n!=0):
	r=n%10
	ans=ans+int(r)
	n=n/10


print(int(ans))