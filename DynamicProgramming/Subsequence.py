S1 = 'ABCIHFEW'
S2 = 'ERNSDDOVJ'

from utils import print_table

def longest_common_substring(s1, s2):
  table = [[None for n in range(len(s2)+1)]for i in range(len(s1)+1)]
  ans = lcs(s1, s2, table) # modifies table
  # fill in None for 0
  for i in range(len(table)):
    for j in range(len(table[0])):
      if not table[i][j]:
        table[i][j] = 0

  print_table(table)


  # traverse_table(table, s1, s2)
  return ans

def traverse_table(table, s1, s2): 
  x = len(s1)
  y = len(s2)
  string = ''

  while not (x == 1 and y == 1):
    if x < 1:
      x = 1
    if y < 1:
      y = 1
    if table[x-1][y] < table[x][y-1]:
      string+= s1[x-1]
      x-=1
    else:
      string+=s1[x-1]
      y-=1
    print(x, y)
  print(string)
  return string

def lcs(s1, s2, table):
  if 0 in [len(s1), len(s2)]: # padding 0s
    table[len(s1)][len(s2)] = 0
    return 0

  if table[len(s1)][len(s2)]: # since 0s padded, ignore 0 based indexing
    return table[len(s1)][len(s2)]

  if s1[-1] == s2[-1]: # if equal, add one
    ans = lcs(s1[:-1], s2[:-1], table) + 1
    table[len(s1)][len(s2)] = ans
    return ans
  
  left = lcs(s1, s2[:-1], table)
  up = lcs (s1[:-1], s2, table)
  diag = lcs(s1[:-1], s2[:-1], table)

  m = max(left, up, diag)
  table[len(s1)][len(s2)] = m 
  return m


longest_common_substring(S1, S2)
print(len(S1))
print(len(S2))