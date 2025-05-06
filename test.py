def expand(i, j):
    while i > 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1: j]


def longest_palindrome_optimal(s):
    if len(s) == 1:
        return s
    temp = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i+1)

        if len(odd) > len(temp):
            temp = odd
        if len(even) > len(temp):
            temp = even
    return temp

s = "abb"
print(longest_palindrome_optimal(s=s))
