from array import *

vals=array('i',[5,9,8,4,2])
print(vals)
print(vals.buffer_info)
print(vals.reverse())
print(vals)

print(vals[0])



val=array('u',['a','b','c','d'])
print(val)


newarray=array(vals.typecode,(a*a for a in vals))

print(newarray)