import math

def linear(x):
  return 5000*x

def n_log_n(n):
  return math.log(n,10)


i = 2

powers = range(0, 100)
values = [2**n for n in powers]
while True:
  if i in values:
    print(i)
  if linear(i) < n_log_n(i):
    print('state')
  i*=2