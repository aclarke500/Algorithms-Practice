'''Happy Valentine's Day! Design a O(log n)-time Divide-and-Conquer algorithm Count-Hearts(V), to find the number of hearts in a string V of stars, represented as S's, and hearts, represented as H's. S's always appear before H's.

Examples: Count-Hearts("SSSSHH") = 2, Count-Hearts("SSSSSSSSSS") = 0, Count-Hearts(HHH) = 3.

A) (10 marks) Write this algorithm in clear pseudo-code.
B) (6 marks) Write the running time of the algorithm T(n) in recurrence relation.
'''

def count_hearts(s):
  if s[len(s)-1] == 'S':
    return 0
  if s[0] == 'H':
    return len(s)
  idx_guess = len(s)//2
  print(idx_guess, 'egg')
  guesses=2
  found = False
  while not found and guesses < 10:
    # over shoot
    if s[idx_guess] == 'S' and idx_guess + 1 == len(s)-1 or s[idx_guess+1] == 'H':
      idx_guess = idx_guess-(len(s)//(2**guesses))
      # print('over', s[idx_guess], s[idx_guess+1], idx_guess)
    # under shoot
    elif s[idx_guess] == 'S':
      idx_guess = idx_guess+(len(s)//2**guesses)
      # print('under', s[idx_guess], s[idx_guess+1], idx_guess)
    # find
    elif s[idx_guess] == 'H' and s[idx_guess+1] == 'S':
      return (len(s)-1) - idx_guess
    
    guesses+=1
    print(idx_guess)
    


print(count_hearts('SSSSSSSHH'))