# ---------------------------------------------------------------------------- #
#                              27. Remove Element                              #
# ---------------------------------------------------------------------------- #

nums = [0,1,2,2,3,0,4,2]
val = 2

count = 0
for i in nums:
    if i == val:
        nums.remove(i)
    


print(len(nums))
print(nums)