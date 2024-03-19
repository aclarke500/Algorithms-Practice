costs = [1,2,4,5,3,9]

def min_cost(costs):
  table = [None] * (len(costs)+1)
  c1 =costs.copy()
  c1.append(0)
  print(c1)
  x= c(len(c1)-1, c1, table)
  print(table)
  return x

def c(n, costs, table):
  if n == 0:
    table[n] = costs[0]
  elif n == 1:
    table[n] = min(costs[0], costs[1])
  elif n == 2:
    table[n] = min(costs[0], costs[1]) + costs[2]

  if table[n]:
    return table[n]
  
  t1 = c(n-1, costs, table)
  t2 = c(n-2, costs, table)

  print(f'For jump {n} with cost {costs[n]} we have {t1} and {t2}.')

  choice = min(t1, t2)
  if n >= len(costs)-1:
    return choice
  table[n]= choice + costs[n]
  return table[n]

print(min_cost(costs))