def climb_stairs(n):
  table = [None] * (n+1)
  return c(n, table)

def c(n, table):
  if n <= 3:
    table[n] = n
  if n == 0:
    table[n] = 1

  if table[n]:
    return table[n]
  
  t = c(n-1, table) + c(n-2, table)
  table[n] = t
  return t

print(climb_stairs(0))

