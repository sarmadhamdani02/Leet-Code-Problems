# ---------------------------------------------------------------------------- #
#                                  69. Sqrt(x)                                 #
# ---------------------------------------------------------------------------- #

class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1

        while i*i <= x:
            if i*i == x:
                return i
            
            i += 1
        
        i -= 1
        print(i)
        
        sqrt = i
        
        return sqrt
    
solution = Solution()
print(f"answer: {solution.mySqrt(4)}")