# can also be solved by temp extran variable
print("By ADDITION and SUBTRACTION")

a=5
b=6

a=a+b
b=a-b
a=a-b

print(a)
print(b)

a=5
b=6

print("By XOR Technique")
a=a^b
b=a^b
a=a^b

print(a)
print(b)

a=5
b=6

print("By Normal python")
a,b=b,a

print(a)
print(b)
