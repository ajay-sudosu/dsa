def remove_duplicates_from_arr(arr):
    seen = set()
    result = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


arr = [1, 1, 2, 2, 3, 3, 3, 4, 5]
print(remove_duplicates_from_arr(arr=arr))
