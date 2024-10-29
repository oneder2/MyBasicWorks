timePoints = ["23:59", "00:00", "19:01"]
    
for i, t in enumerate(timePoints):
    timePoints[i] = int(t[:2]) * 60 + int(t[3:])

timePoints.sort()

minDiff = 1440 - timePoints[len(timePoints)-1] + timePoints[0]

for i in range(0, len(timePoints) - 1):
    diff = timePoints[i+1] - timePoints[i]
    if diff < minDiff:
        minDiff = diff

print(timePoints)
print(minDiff)
# return(minDiff)