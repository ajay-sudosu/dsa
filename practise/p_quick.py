def quick(arr):
    if len(arr) <= 1:
        return arr

    left, right, pivot = [], [], arr[-1]

    for i in arr[:-1]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    return quick(left) + [pivot] + quick(right)


if __name__ == "__main__":
    result = quick(arr=[4, 3, 1, 6, 2, 5])
    print(result)
