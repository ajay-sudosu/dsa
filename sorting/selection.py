def selection_sort(arr):
    for i in range(len(l) - 1):
        index = i
        for j in range(i+1, len(l)):
            if arr[index] > arr[j]:
                index = j
        # arr[index], arr[i] = arr[i], arr[index]
        arr[i], arr[index] = arr[index], arr[i]
    print(arr)
    return arr


if __name__ == "__main__":
    l = [20, 0, 15, 10, 5, 40, 1]
    selection_sort(l)
