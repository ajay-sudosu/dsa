"""
This is a naive solution (first try)
"""

st = "eeeeeeee"


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
Here is a better approach
"""


def longest_palindrome_op(s: str):
    ...
