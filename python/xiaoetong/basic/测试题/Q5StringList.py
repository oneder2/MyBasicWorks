string_list = ["apple", "banana", "cherry", "date", "elderberry"]

longest = 0
longestWord = ""
for word in string_list:
    if longest < len(word):
        longest = len(word)
        longestWord = word

print(longestWord)