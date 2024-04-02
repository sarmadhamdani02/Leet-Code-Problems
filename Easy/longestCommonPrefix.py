# -- longest common prefix - #

strs = []

def longestCommonPrefix(strs):
    res = ""
    for i in range(len(min(strs, key=len))):
        for s in strs:
            if s[i] != strs[0][i]:
                return res
        
        res += strs[0][i]
    return res



print(longestCommonPrefix(strs))