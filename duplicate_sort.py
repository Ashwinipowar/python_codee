#method 1
nums=[1,2,2,3,1,3,4,5,5,6,7,7,8,8,9]
n=len(nums)
freq_map={}
for i in range (0,n):
    freq_map[nums[i]]=0
j=0
 
for k in freq_map:
    nums[j]=k
    j+=1
print(j)





#optimized way
nums=[1,2,2,3,1,3,4,5,5,6,7,7,8,8,9]
n=len(nums)
if n==i:
    print(1)
i=0
j=i+1
while j< n:
    if nums[j]!= nums[i]:
     i+=1
nums[i],nums[j]=nums[j],nums[i]
j+=1
print(i+1)