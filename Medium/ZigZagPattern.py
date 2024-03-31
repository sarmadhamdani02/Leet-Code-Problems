
numRows = 4
s = "PAYPALISHIRING" 


for i in range(0, len(s), (numRows+1)):
    print(s[i], end=" ")
print()

for j in range(1,len(s), (numRows-1)):
    print(s[j], end=" ")
print()


for i in range(2, len(s), (numRows+1)):
    print(s[i], end=" ")
print()

