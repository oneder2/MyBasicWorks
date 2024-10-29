# ①
# if condition => bool:
#     # then
#     do sth

# ②
user_name = input("Please type in your name:")
try:
    user_age = int(input("Please type in your age:"))
except ValueError:
    print("Bad input")

if user_age > 64:
    print("retire")
elif 0 < user_age <= 64:
    print("go on")
else:
    print("Bad input")

# ③
score = input("please type in your score")
if score < 60:
    print("disqualified")
elif 60 <= score < 70:
    print("qualified")
elif 70 <= score < 80:
    print("good")
elif 80 <= score < 90:
    print("very good")
elif 90 <= score <= 100:
    print("outstanding")
else:
    print("Bad input")
