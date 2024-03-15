import math
i = 'agagaagaggagaggaggaggaaggaaag'
print(i.count('a'))
print(i.count('g'))
def find_letter(s):
  # base case
  if len(s) < 5:
    max = (None, 0)
    for c in s:
      if s.count(c) >= len(s)//2:
        return c
    print('s', s)
    return False
  
  # divide
  mid = math.floor(len(s)/2)
  s1 = s[:mid]
  s2 = s[mid:]

  # conquer
  r1 = find_letter(s1)
  r2 = find_letter(s2)
  if s1 and s1.count(r1) >= len(s) // 2:
    return r1
  elif s2 and s2.count(r2) >= len(s) // 2:
    return r2
  # combine
  # s1 = sorted(s)


print(find_letter(i))