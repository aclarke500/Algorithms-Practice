s1 = 'ABACABB'
s2 = 'ABACCABABBAB'
s3 ='f'

def longest_substring(s1, s2):
  data = [[None for n in s2] for i in s1]
  return lcsl(s1, s2, data)
  

def lcsl(s1, s2, data):
  if 0 in [len(s1), len(s2)]:
    print('state')
    return 0

  if len(s1) == 1:
    res = int(s1[0] in s2)
    data[len(s1)][len(s2)] = res
    return int(s1[0] in s2)
  if len(s2) == 1:
    res = int(s2[0] in s1)
    data[len(s2)][len(s1)] = res
    return res
  
  if data[len(s1)-1][len(s2)-1]:
    return data[len(s1)-1][len(s2)-1]
  
  if s1[len(s1)-2] == s2[len(s2) -2]:
    res = lcsl(s1[0:len(s1)-2], s2[0:len(s2)-2], data) + 1
    data[len(s1)-1][len(s2)-1] = res
    return res
  
  a = lcsl(s1[0:len(s1)], s2[0:len(s2)-1], data)
  b = lcsl(s1[0:len(s1)-1], s2[0:len(s2)], data)

  if a > b:
    data[len(s1)-1][len(s2)-1] = a
    return a
  data[len(s1)-1][len(s2)-1] = b
  return b
  

print(longest_substring(s1, s2))

