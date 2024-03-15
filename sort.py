'''Given a list s of sorted integers, where there are duplicates, count the
occurrences of a given number k.
Examples: Input ([1,1,1,3,3,3,5], 3) returns 3
Input ([6,6,6,8,8,10,10,10,10], 8) returns 2
'''

def count(input,k):
  # divide
  left_idx = get_left(input, k)
  print(left_idx)
  right_idx = get_right(input, k)
  return right_idx - left_idx

def get_left(input, k):
  left = len(input)//2
  if input[left] == k and input[left-1] < k:
    return left
  elif input[left] < k:
    return get_left(input[left:],k)
  else:
    return get_left(input[:left],k)
  
def get_right(input, k):
  right = len(input)//2
  if input[right] == k and input[right+1] > k:
    return right
  elif input[right] > k: # overshoot
    return get_right(input[:right], k)
  elif input[right] <= k:
    return get_right(input[right:], k)
  

input = [1,1,1,1,2,2,2,3,3,3,3,5,5,5,5]
print(count(input, 3))