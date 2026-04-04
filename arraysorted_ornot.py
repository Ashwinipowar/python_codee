nums = [33, 4, 5, 6, 78, 32, 3, 4, 5]
n = len(nums)

for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        print(False)
        break
else:
    print(True)

  


nums = [3, 4, 5, 6, 7, 8, 9]
n = len(nums)

for i in range(0, n-1):
    if nums[i] > nums[i+1]:
        print(False)
        break
else:
    print(True)







#thodasa advanced

def is_sorted(nums):
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

# Usage
nums = [33, 4, 5, 6, 78, 32, 3, 4, 5]
print(is_sorted(nums))  # Output: False
# all() function returns True only if all comparisons are True.
# nums[i] <= nums[i+1] checks every adjacent pair
         