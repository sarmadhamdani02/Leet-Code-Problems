
def isValid(s):
    stack = []
    map = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for char in s:

        if char in map:
            if stack and stack[-1] == map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return False if len(stack) > 0 else True

        
s = str(input("> "))

print(isValid(s))