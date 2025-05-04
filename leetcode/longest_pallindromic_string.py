"""
This is a naive solution (first try)
"""


st = "abba"


def longest_palindrome(s: str):
    n = s[0]
    for i in range(len(s) - 1):
        j = i+1
        while j <= len(s) - 1:
            left = i
            right = j
            temp = ''
            pall = False
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    pall = True
                else:
                    break
            else:
                if pall:
                    temp = s[i:j+1]
                    if not n:
                        n = temp
                    else:
                        if len(temp) > len(n):
                            n = temp
            j += 1
    return n


# print(longest_palindrome(s=st))


"""
Better approach
"""


def longest_palindrome_optimal(s: str):
    if len(s) <= 1:
        return s

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

    n = s[0]
    for i in range(len(s) - 1):
        even_expansion = expand(i, i+1)
        odd_expansion = expand(i, i)
        if len(even_expansion) > len(n):
            n = even_expansion

        if len(odd_expansion) > len(n):
            n = odd_expansion
    return n


b = "abb"
print(longest_palindrome_optimal(s=b))
