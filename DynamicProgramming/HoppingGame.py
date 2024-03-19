def hop(n, table):
  if n <= 2:
    table[n] = n

  if table[n]:
    return table[n]
  
  table[n] = hop(n-1, table) + hop(n-2, table)
  return table[n]

def hop_caller(n):
  table = [None] * (n+1)
  return (hop(n, table), table)

print(hop_caller(4))