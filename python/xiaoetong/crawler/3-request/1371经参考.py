s = "eleetminicoworoep"

mask = 0
charDic = {"a":1,"e":2,"i":4,"o":8,"u":16}

firstOccurance = {0: -1}
maxLen = 0

for i, c in enumerate(s):
    if c in charDic:
        mask ^= charDic[c]
    
    if mask in firstOccurance:
        maxLen = max(maxLen, i - firstOccurance[mask])

    else:
        firstOccurance[mask] = i

print(maxLen)