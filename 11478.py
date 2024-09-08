s = input()

substrs = set()

for i in range(len(s)):
    substr = ''
    for j in range(i, len(s)):
        substr += s[j]
        substrs.add(substr)

print(len(substrs))