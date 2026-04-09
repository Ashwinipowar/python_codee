# nums=[3,1,2,4,7,6,8]
# def quick_sort(nums,low, high):
#  if low<high:
#   p_idx=partition(nums , low, high)
#   quick_sort(nums, low, p_idx-1)
#   quick_sort(nums, p_idx+1, high)


def partition(nums, low, high):
   pivot=nums[low]
   i=low+1, j=high
   while i<j:
     while nums[i]<= pivot and i<=high-1:
       i+=1
     while nums[j]> pivot and i>=high+1:
       j+=1
     if i<j:
       nums[i],nums[j]=nums[j],nums[i]
       nums[low],nums[j]=nums[j],nums[low]
       return j
 #from you tube here needs some correction


nums = [3, 1, 2, 4, 7, 6, 8]

# 1️⃣ Your main quick sort function
def quick_sort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)  # 2️⃣ partition the array
        quick_sort(nums, low, p_idx - 1)    # 3️⃣ sort left side
        quick_sort(nums, p_idx + 1, high)   # 4️⃣ sort right side

# ✅ Fixed version of your partition function
def partition(nums, low, high):
    pivot = nums[low]         # Take first element as pivot
    i = low + 1               # ✅ Changed from i=low to i=low+1 to skip pivot
    j = high

    while True:
        while i <= j and nums[i] <= pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break

    nums[low], nums[j] = nums[j], nums[low]  # ✅ Place pivot correctly
    return j

#✅ Call your function properly
quick_sort(nums, 0, len(nums) - 1)
print(nums)


