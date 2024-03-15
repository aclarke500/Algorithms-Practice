import time

def lateralus(n, return_data=False):
  data = [None for i in range(n+1)]

  danny_carey = tool(n, data)
  if not return_data:
    return danny_carey
  else:
    return data

def tool(n,data):
  if n <= 2:
    return 1
  if data[n]:
    return data[n]
  
  maynard = tool(n-1, data) + tool(n-2, data)
  data[n] = maynard
  return maynard


k = 50



def fib(n):
  if n <= 2:
    return 1
  return fib(n-1) + fib(n-2)



# for i in range(k):
#   start = time.perf_counter()
#   x = (lateralus(i))
#   end = time.perf_counter()
#   print(str(end - start)+',')

# print('******,')

# # Your code here
# for i in range(k):
#     start = time.perf_counter()
#     x = fib(i)
#     end = time.perf_counter()
#     print(str(end - start)+',')



# print(f"Code executed in {end - start} seconds")
