s = "au"

if s == "":
    print("00")

globalMax = 0
localMax = 0
visited = {}

for i in range(len(s)):
    if s[i] in visited and visited[s[i]] >= i - localMax:
        globalMax = max(globalMax, localMax)
        localMax = i - visited[s[i]]
    else:
        localMax += 1
    visited[s[i]] = i

globalMax = max(globalMax, localMax)

print(globalMax)
