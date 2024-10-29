s1 = "apple is is"
s2 = "this apple is sour"


s1_l = s1.split(" ")
s2_l = s2.split(" ")

count = dict()
diff = []

for i in s1_l:
    if not i in count:
        count[i] = 1
    else:
        count[i] = count[i] + 1

for i in s2_l:
    if not i in count:
        count[i] = 1
    else:
        count[i] = count[i] + 1

for i in count:
    if count[i] == 1:
        diff.append(i)

print(count)
print(diff)
