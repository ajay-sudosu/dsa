def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0
    start =0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if max_length < right - left + 1:
            start = left
            max_length = right - left + 1

    return s[start:max_length+start]


s = "bcdabc"
print(longest_substring_without_repeating(s))
