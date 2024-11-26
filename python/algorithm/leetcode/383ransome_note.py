from collections import Counter


def myCanConstruct(ransomNote: str, magazine: str) -> bool:
    ran = {}
    for char in ransomNote:
        if char in ran:
            ran[char] += 1
        else:
            ran[char] = 1

    mag = {}
    for char in magazine:
        if char in mag:
            mag[char] += 1
        else:
            mag[char] = 1
    
    print(ran)
    print(mag)
    for char in ran:
        if not(char in mag and mag[char] >= ran[char]):
            return False
    return True


def bitCanConstruct(ransomNote: str, magazine: str) -> bool:
    ran = Counter(ransomNote)
    mag = Counter(magazine)
    if ran & mag == ran:
        return True
    return False


#print(canConstruct("aa", "aab"))
print(bitCanConstruct("aa", "ab"))







