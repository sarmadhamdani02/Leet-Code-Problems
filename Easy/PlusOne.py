# ---------------------------------------------------------------------------- #
#                                 66. Plus One                                 #
# ---------------------------------------------------------------------------- #

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break  # Break out of the loop after adding one to a non-9 digit
        else:  # This else block runs if the loop completes without breaking
            digits.insert(0, 1)  # If all digits are 9, add 1 at the beginning
        return digits
    
solution  =Solution()
print(solution.plusOne([1,9,9,9,9,9]))
