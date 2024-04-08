
# ---------------------------------------------------------------------------- #
#                          35. Search Insert Position                          #
# ---------------------------------------------------------------------------- #




def searchInsert(nums, target):
    i = 0
    j = len(nums) - 1
    
    while i <= j:
        mid = (i + j) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            i = mid + 1
            
        else:
            j = mid - 1
            
    return i

# Example usage:
nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))  # Output: 1


