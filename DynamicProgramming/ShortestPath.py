import math

def caller(grid):
  dp = []
  for g in grid:
    g_arr = []
    for gi in g:
      g_arr.append(None)
    dp.append(g_arr)
  x = len(grid[0])
  y = len(grid)
  print(dp)
  print(x, y)
  return (path(x-1, y-1, dp, grid), dp)

def path(x, y, dp, grid):
 
  if x < 0 or y < 0:
    return math.inf
  if dp[x][y]:
    return dp[x][y]
  
  if x == 0 and y == 0:
    dp[0][0] = grid[0][0]
    return grid[0][0]
  
  if x == 0:
    c = path(x, y-1, dp, grid) + grid[x][y]
    dp[x][y] = c
    return c
  if y == 0:
    c = path(x-1, y, dp, grid) + grid[x][y]
    dp[x][y] = c
    return c
  t1 = path(x-1, y, dp, grid)
  t2 = path(x, y-1, dp, grid)
  dp[x][y] = min(t1, t2) + grid[x][y]
  return dp[x][y]
  

def traverse(dp, path):
  x = len(dp[0])-1
  y = len(dp)-1
  while not (x == 0 and y == 0):
    if x == 0:
      y-=1
      path.append(dp[x][y])
      continue
    if y == 0:
      x-=1
      path.append(dp[x][y])
      continue
    t1 = dp[x-1][y]
    t2 = dp[x][y-1]
    if t1 < t2:
      x-=1
      path.append(dp[x][y])
      continue
    else:
      y-=1
      path.append(dp[x][y])
      continue
  path.insert(0, dp[len(dp[0])-1][len(dp)-1])
  return path



g = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1],
  [9,5,2]
]

x = (caller(g))
print(x[0])
for g in x[1]:
  print(g)

print(traverse(x[1], []))