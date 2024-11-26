raw = input()
rawInput = raw.replace("-", "")

added = 0
for i in range(0, len(rawInput) - 1):
    added += int(rawInput[i]) * (i+1)
moding = str(added % 11)

if moding == "10":
    moding = "X"

if moding == rawInput[-1]:
    print("Right")
else:
    print(raw[0:12] + moding)
