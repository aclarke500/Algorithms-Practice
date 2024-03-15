radii = [2,	2,	1,	1,	1,	3]


def covered_by(tree, shrub):
  min_range = tree[1] - tree[0]
  max_range = tree[1] + tree[0]
  return shrub[1] >= min_range and shrub[1] <= max_range

def covered(turned_on, light):
  for tup in turned_on:
    if covered_by(tup, light):
      return True
    
  return False

x = (5, 65)
y = (0, 63)

print(covered_by(x,y))
print(covered_by(y,x))

def min_lamp(r):
  tups = []
  for i in range(len(r)):
    left = i - r[i]
    right = i + r[i]
    if left < 0: left = 0 
    if right > len(r): right = len(r)
    tups.append((i, left, right, right-left))

  # sort tups by 2nd element
  T = sorted(tups, key=lambda tup: tup[1])

  turned_on = []
  covered_end = False
  curr_left = 0

  while not covered_end:
    relevant_lights = list(filter(lambda tup: tup[1] == curr_left, T))
    if not len(relevant_lights):
      return None
    greedy_choice = max(relevant_lights, key=lambda light: light[2])
    curr_left += greedy_choice[3]
    turned_on.append(greedy_choice)
    if greedy_choice[2] >= len(r): 
      covered_end = True
  

  return [tup[0] for tup in turned_on]
print(min_lamp(radii))

