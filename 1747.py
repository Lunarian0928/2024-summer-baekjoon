max_size = 10 ** 7
is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, max_size + 1):
    if (is_prime[i]):
        for j in range(i + i, max_size + 1, i):
            is_prime[j] = False

    
def is_palindrome(n):
    str_n = str(n)
    if (str_n == str_n[::-1]):
        return True
    return False

n = int(input())

while True:
    if (is_prime[n]) and (is_palindrome(n)):
        print(n)
        break
    n += 1