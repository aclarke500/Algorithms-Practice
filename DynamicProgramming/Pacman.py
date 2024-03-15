
def pacman(grid):
  table = [[None for n in grid] for g in grid[0]]
  x= p(0,0, grid, table)
  for t in table:
    print(t)
  return x

def p(i, j, grid, table):
  n = len(grid)
  if n - i < 2 and n - j < 2:
    base_case(grid, table, n)

  if table[i][j]:
    return table[i][j]
  
  if grid[i][j]: # if ghost, no paths from this point
    table[i][j] = 0
    return 0
  
  if n - i == 1: # right wall, corner captured by base case
    ans = p(i, j+1, grid, table)
    table[i][j] = ans
    return ans
  elif n - j == 1: # floor
    ans = p(i+1, j, grid, table)
    table[i][j] = ans
    return ans
  # if not on edge, sum two other paths
  above = p(i, j+1, grid, table)
  right = p(i+1, j, grid, table)
  table[i][j]= above+right
  return above+right


def base_case(grid, table, n):
  if grid[n-1][n-1] == 1:
    table[n-1][n-1] = 0
  else:
    table[n-1][n-1] = 1

  if grid[n-1][n-2] == 1:
    table[n-1][n-2] = 0
  else:
    table[n-1][n-2] = 1

  if grid[n-2][n-1] == 1:
    table[n-2][n-1] = 0
  else:
    table[n-2][n-1] = 1

  if grid[n-2][n-2] == 1:
    table[n-2][n-2] = 0
  else:
    table[n-2][n-2] = 2
print(pacman([[0, 1], [0,0]]))