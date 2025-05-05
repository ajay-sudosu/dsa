def longestCommonPrefix(strs) -> str:
    ra = min([len(i) for i in strs])
    min_element = [i for i in strs if len(i) == ra][0]
    s = ""
    for i in range(ra):
        element = min_element[i]
        index = 0
        while index < len(strs):
            if strs[index][i] == element:
                index += 1
            else:
                return s
        else:
            s = s + element
    return s


# exp = ["flower", "flow", "flight"]
exp = ["cir", "car"]
result = longestCommonPrefix(strs=exp)
print(result)
