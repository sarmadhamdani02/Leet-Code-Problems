class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            if char in bracketMap.values():  # Check if the character is an opening bracket
                stack.append(char)
            elif char in bracketMap.keys():  # Check if the character is a closing bracket
                if not stack or stack.pop() != bracketMap[char]:
                    return False  # Mismatched brackets
        return not stack  # Return True if the stack is empty, False otherwise

solution = Solution()
print(solution.isValid("()"))  # Output: True
