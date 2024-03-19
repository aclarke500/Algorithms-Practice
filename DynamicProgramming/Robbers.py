values = [1,5,2,2,58]

def rob(values):
  table = [None] * (len(values))
  return r(len(values)-1,values,table)

def r(i, values, table):
  if i < 0:
    return 0
  if i == 0:
    table[i] = values[i]
    return table[i]
  if i == 1:
    table[i] = max(values[0], values[1])
    return table[i]
  if i == 2:
    t1 = values[0] + values[2]
    t2 = values[1]
    table[i] = max(t1, t2)
    return table[i]

  if table[i]:
    return table[i]
  
  t1 = r(i-2, values, table)
  t2 = r(i-3, values, table)
  table[i] = max(t1, t2) + values[i]
  return table[i]

print(rob(values))