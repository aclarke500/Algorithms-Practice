vector = [1, 12, 2, 4, 21]

def lis(v):
  table = [None for vi in v]
  return lis_helper(v, table)


def lis_helper(v, table):
  # base cases: first element or in lookup table
  if len(v) == 1:
    table[0] = [v[0]]
  if len(v) == 0:
    return []
  if table[len(v)-1]:
    return table[len(v)-1]
  # find best choice to append to
  options = []
  
  for i in range(len(v)-1):
    o = validate_choice(i, v[:i+1], table)
    options.append(o)
  scores = [len(option) for option in options]
  m = max(scores)
  i = scores.index(m)

  ideal_sublist =options[i].copy()
  ideal_sublist.append(v[-1])
  if check_list(ideal_sublist):
    table[len(v)-1] = ideal_sublist
  return ideal_sublist

def validate_choice(i, v, table):
  if len(v) == 3:
    print('eggs for dinner')
  if len(v) == 0:
    return []
  if not len(v) or v[i] > v[-1] :
    return []
  x = lis_helper(v[:i+1], table)
  if check_list(x):
    return x
  return []

def check_list(list):
  for i in range(len(list)):
    if i == 0:
      continue
    if list[i] <=list[i-1]:
      return False
  return True

# print(lis(vector))

def length_of_longest_substring(v, table):
  if len(v) <= 1:
    table[len(v)-1] = 1
    return 1
  if table[len(v)-1]:
    return table[len(v)-1]
  
  max = 0
  for i in range(len(v)-1):
    x = length_of_longest_substring(v[:i+1], table)
    if v[i] < v[-1]: # x is the length of a VALID subsequence
      max = x
  table[len(v)-1] = max+1
  return max+1

table = [None for v in vector]
print(length_of_longest_substring(vector, table))
print(table)

  
