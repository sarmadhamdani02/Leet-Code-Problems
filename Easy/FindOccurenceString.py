# ---------------------------------------------------------------------------- #
#            28. Find the Index of the First Occurrence in a String            #
# ---------------------------------------------------------------------------- #

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        try:
            index = haystack.index(needle)
            return index
        except:
            return -1

solution = Solution()
print(solution.strStr("abc", "c"))

