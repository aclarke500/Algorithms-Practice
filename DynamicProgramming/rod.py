lengths = [1,2,3,4,5]
price = [3,4,5,1,9]

def find_combinations(target, current_combination=[], start=1):
    # Base case: if target sum is reached, print the combination
    if target == 0:
        print(current_combination)
        return

    # Explore further only if remaining target is positive
    if target > 0:
        for i in range(start, target + 1):
            # Include the current number and explore further
            find_combinations(target - i, current_combination + [i], i)

def rod_cut(lenghts, price, n):
    opt_price = [None for i in lengths]
    
    
