is_palindrome = 1
word = input()
for i in range(0, len(word) // 2):
    if (word[i] != word[-1 - i]):
        is_palindrome = 0
        break
    
print(is_palindrome)