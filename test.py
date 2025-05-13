def sort(arr):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr


print(sort(arr=[3, 2, 1, 6, 0]))
