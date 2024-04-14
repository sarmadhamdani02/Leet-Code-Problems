# ---------------------------------------------------------------------------- #
#                            58. Length of Last Word                           #
# ---------------------------------------------------------------------------- #

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        
        s = ' '.join(s.split())
        i = len(s) - 1
        while i >= 0 and i <= (len(s) - 1):

            if s[i] == " ":
                return length
            
            length += 1
            i -= 1
        return length


solution = Solution()
print(solution.lengthOfLastWord("   fly me   to   the moon  "))