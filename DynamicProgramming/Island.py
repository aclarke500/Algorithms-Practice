costs = [10, 10, 40, 33, 15, 1]


def quickest_path(costs):
  costs.append(0)
  lookup_table = [None for c in costs]
  cost = cost_to_reach(len(costs)-1, lookup_table, costs)
  return cost

def cost_to_reach(n, opt_cost, costs, hop_str = ''):
  if n  == 0: # base case
    opt_cost[n] = 0
    return (0, '0')
  elif n == 1:
    opt_cost[n] = costs[n-1]
    return (costs[n-1], '1')

  
  if n < 0:
    return 999999999
  
  if opt_cost[n]: # lookup if applicable
    return opt_cost[n]

  # recurse
  one_hop = cost_to_reach(n-1, opt_cost, costs, hop_str)
  print(one_hop)
  one_hop = one_hop[0]+costs[n-1]

  two_hop = cost_to_reach(n-2, opt_cost, costs, hop_str)[0] + costs[n-2]

  choice = None
  if one_hop < two_hop:
    choice = one_hop
    hop_str += str(n-1)
  else:
    choice = two_hop
    hop_str += str(n-2)
  choice = min(one_hop, two_hop)

  opt_cost[n] = choice
  return (choice, hop_str)


print(quickest_path(costs))
print(quickest_path([15, 3, 11, 36]))
print(quickest_path([15, 3, 11, 36, 2, 18]))



  
