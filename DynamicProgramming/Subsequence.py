S1 = 'ABCDEF'
S2 = 'ABACADE'

def longest_common_substring(s1, s2):
  table = [[None for n in range(len(s2)+1)]for i in range(len(s1)+1)]
  print(lcs(s1, s2, table))

def lcs(s1, s2, table):
  if 0 in [len(s1), len(s2)]: # padding 0s
    table[len(s1)][len(s2)] = 0
    return 0

  if table[len(s1)][len(s2)]:
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