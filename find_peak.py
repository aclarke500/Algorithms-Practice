def findPeakElement(nums):
    
  return findPeakUtil(0, len(nums) - 1, nums)

def findPeakUtil(low, high, nums):
        # Your divide and conquer logic here
        guess_idx = low + (high - low)//2 
        if guess_idx == len(nums) -1 or guess_idx == 0:
             return None
        elif nums[guess_idx-1] < nums[guess_idx] > nums[guess_idx+1]:
             return guess_idx
        else:
            if findPeakUtil(low, guess_idx, nums):
                 return findPeakUtil(low, guess_idx, nums)
            elif findPeakUtil(guess_idx, high, nums):
                 return findPeakUtil(guess_idx, high, nums)


# Test the function
nums = [1,2,3,4,5,4,3,2,1]
# print(findPeakElement(nums))

def findMin(nums):
    # Your divide and conquer (binary search) logic here
    return findMinUtil(0, len(nums)-1, nums)

def findMinUtil(left, right, nums):
    guess_idx = left + (right - left)//2
    if nums[guess_idx] < nums[guess_idx+1] and nums[guess_idx] < nums[guess_idx-1]:
        return nums[guess_idx]
    elif nums[len(nums)-1] < nums[len(nums)-2]:
         return nums[len(nums)-2]

    elif nums[guess_idx] < nums[len(nums)-1]: 
      return findMinUtil(left, guess_idx, nums)
    else:
        return findMinUtil(guess_idx, right, nums)

# Test the function with examples
# print(findMin([3,4,5,1,2]))  # Expected output: 1
# print(findMin([4,5,6,7,0,1,2]))  # Expected output: 0
# print(findMin([11,13,15,17]))  # Expected output: 11


def maxSubArray(nums):
    # Helper function to use in the divide and conquer approach
    def maxCrossingSum(nums, left, mid, right):
        # Calculate the max crossing sum from the middle
        pass
    
    def maxSubArraySum(nums, left, right):
        # Base case: when there is only one element
        if left == right:
            return nums[left]
        
        # Find middle point
        mid = (left + right) // 2
        
        # Return maximum of following three possible cases
        # 1. Maximum subarray sum in left half
        # 2. Maximum subarray sum in right half
        # 3. Maximum subarray sum such that the subarray crosses the midpoint
        return max(maxSubArraySum(nums, left, mid),
                   maxSubArraySum(nums, mid+1, right),
                   maxCrossingSum(nums, left, mid, right))
    
    return maxSubArraySum(nums, 0, len(nums)-1)

# Test the function with an example
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Expected output: 6

