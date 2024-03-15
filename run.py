import math

sum=0

for i in range(10):
  sum+=((2**i)/3**i)

print(sum)

cf = (2**(10)-1)/((3**(10)-1)/2)
two = 2**(10)-1
three = (3**(10)-1)
# print(two, three)
print(two/three)
print(cf)