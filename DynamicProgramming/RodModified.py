def rod(n, p, c):
  opt_cut = [None for i in range(n)]
  return rod_helper(n, p, opt_cut, c)

def rod_helper(n, p, d, c):
  if n == 1:
    return p[n]
  if d[n-1]:
    return d[n-1]
  
  combos = []
  for i in range(n):
    if i == 0 or i == n-1:
      combos.append(p[i])
    else:
      temp = rod_helper(i, p, d, c)
      add = p[n-i] + c
      combos.append(temp+add)

  m = max(combos)
  d[n-1] = m
  return m


p = [2,3,4,5]
c = 5
print(rod(4, p, c))