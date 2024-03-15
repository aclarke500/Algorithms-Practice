# I = 'aabbccddffgghhaabbccddffgghhaabbccddffgghhaabbccddffgghhaabbccddffgghheaabbccddffgghhaabbccddffgghhaabbccddffgghhaabbccddffgghh'

I='aabbcceddffgghh'
import math
# def find_single_letter(string, depth=0):
#   # base case n = 5
#   if len(string) <= 5:
#     for s in range(len(string)):
#       if s < len(string)-1 and s > 0:
#         if string[s] not in [string[s+1], string[s-1]]:


#   # divide
#   # conquer
#   # return

# we MUST have an odd number to begin with
# if middle element is NOT the s+1, check if s not s-1
# if not, recurse to s/2

# def find_single_letter(data):
#   print(data)
#   if len(data) == 4:
#     if data[0] != data[1]:
#       return 0, data[0]
#     elif data[2] and data[3] and data[2] != data[3]:
#       return 2, data[2]
#     else:
#       return False
#   elif data[len(data)-1] != data[len(data)-2]:
#     return len(data)-1, data[len(data)-1]

#   mid = math.ceil(len(data)/2)
#   if data[mid-1] != data[mid]:
#     # we've found proof of violation before
#     # 2 cases
#     # 1 we violated here
#     if data[mid] != data[mid-1]:
#       return mid, data[mid]
#     # 2 violate before
#     else:
#       return find_single_letter(data[:mid])
#   return find_single_letter(data[mid+1:])


def find_single_letter(data):
  if len(data)%2 == 0:
    return None, None
  l = len(data)
  mid = math.floor(len(data)/2)-1 # this will be middle w/ 0-index
  d= data[mid]
  dat = [data[mid-1], data[mid], data[mid+1]]
  eg = [data[mid-1], data[mid+1]]
  mid = math.floor(len(data)/2) # this will be middle w/ 0-index
  ls = data[mid] == data[mid+1]
  rs = data[mid-1] == data[mid]
  if not (data[mid] == data[mid+1] or data[mid-1] == data[mid]):
    return mid, data[mid]
  elif data[mid] == data[mid+1]:
    find_single_letter(data[mid:]) # assume inclusivie
  elif data[mid] == data[mid-1]:
    find_single_letter(data[:mid])
print(find_single_letter(I))
