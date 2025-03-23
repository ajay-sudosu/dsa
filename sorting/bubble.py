def bubble_sort(l):
    count = 0
    print("Normal Bubble sort:: Before:", l)
    for i in range(len(l)):
        for j in range(len(l) - 1):
            count += 1
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    print("Normal Bubble sort:: After:", l)
    print("Total Iterations:", count)
    return l


def bubble_sort_modified(l):
    count = 0
    print("Modified Bubble sort:: Before:", l)
    for i in range(len(l)):
        change = False
        for j in range(len(l) - 1):
            count += 1
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                change = True
        else:
            if not change:
                break

    print("Total Iterations:", count)
    print("Modified Bubble sort:: After:", l)
    return l


if __name__ == "__main__":
    # driver code
    arr = [16, 20, 15, 10, 15, 25]
    bubble_sort(arr)
    bubble_sort_modified(arr)
