def insertion_sort(arr):
    print("Normal Insertion sort:: Before:", arr)
    count = 0
    for i in range(len(arr) - 1):
        j = i + 1
        while j > 0:
            count += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    print("Iteration count", count)
    print("Normal Insertion sort:: After:", arr)
    return arr


def insertion_sort_modified(arr):
    print("Modified Insertion sort:: Before:", arr)
    count = 0
    for i in range(len(arr) - 1):
        j = i + 1
        while j > 0:
            count += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break

    print("Iteration count", count)
    print("Modified Insertion sort:: After:", arr)
    return arr


if __name__ == "__main__":
    l = [33, -1, 12, 50, 34, 10, 1, 0, 4]
    # insertion_sort(arr=l)
    insertion_sort_modified(arr=l)
