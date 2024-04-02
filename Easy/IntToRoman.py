# ~~~~~~~ 14. Longest Common Prefix ~~~~~~~ #

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        minimumLength = min(strs, key=len)
        print(minimumLength)

    




solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))