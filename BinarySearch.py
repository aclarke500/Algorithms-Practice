s = [n for n in range(1, 10001)]
print('eg')

def binary_search(s, k):
  guess = len(s)//2
  trials = 1

  while s[guess] != k:
    trials+=1
    print(guess)
    if s[guess] > k:
      guess = (guess - len(s)//(2**trials))
      print(guess)

    elif s[guess] < k:
      guess = (guess + len(s)//(2**trials))
      print(guess)

  return guess

data = [1,1,1,3,3,3,5,5,5,6,6,6,7,7,7,7,7,7,7,8,8]
def count_occurences(s, k):
  guess = len(s)//2
  trials = 1

  while s[guess] != k:
    trials+=1
    if s[guess] > k:
      guess = (guess - len(s)//(2**trials))

    elif s[guess] < k:
      guess = (guess + len(s)//(2**trials))

  upper_bound = guess
  guess = len(s)//2
  trials = 1
  found = False
  while not found:
    # print(s[guess], guess, trials)
    if s[guess] < k and s[guess+1] is k:
      found = True

    elif s[guess] >= k:
      guess = (guess - upper_bound//(2**trials))

    elif s[guess] < k:
      guess = guess + upper_bound//(2**trials)

    trials +=1

  lower_bound = guess+1 # first k
  print('sate')
  trials = 1
  found = False
  guess = len(s)//2
  while not found:
    print(s[guess], guess, trials)
    if s[guess] > k and s[guess-1] is k:
      found = True

    elif s[guess] >= k:
      guess = (guess - len(s)//(2**trials))

    elif s[guess] < k:
      guess = guess + len(s)//(2**trials)

    trials +=1

  return upper_bound - lower_bound


print(count_occurences(data, 7))
