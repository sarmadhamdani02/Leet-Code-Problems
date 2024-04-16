# ---------------------------------------------------------------------------- #
#                                67. Add Binary                                #
# ---------------------------------------------------------------------------- #

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = ""
        carry = 0  # Initialize the carry
        
        # Iterate through the digits of a and b simultaneously from right to left
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            # Calculate the sum of the current digits and the carry
            digit_sum = carry
            
            if i >= 0:
                digit_sum += int(a[i])
                i -= 1
            if j >= 0:
                digit_sum += int(b[j])
                j -= 1
            
            # Append the appropriate digit to the result and update the carry
            c = str(digit_sum % 2) + c
            carry = digit_sum // 2
        
        return c

solution = Solution()
print(solution.addBinary("110", "11")) # 1001
