def isPrime(num):
    if  num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


length = int(input())
input_nums = input().strip(" ").split(" ")
input_nums = list(map(int, input_nums))
prime_list = list(filter(isPrime, input_nums))
prime_list = list(map(str, prime_list))
print(" ".join(prime_list))



