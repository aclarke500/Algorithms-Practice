def minimum_coins(value):
  denominations = [0.05, 0.10, 0.25, 1, 2]
  # denominations.sort(reverse=True)
  change = []
  value_left = value
  while value_left > 0:
    m = None
    for d in denominations:
      if d <= value_left:
        m = d

    change.append(m)
    value_left-=m

  print(change)

minimum_coins(3.65)