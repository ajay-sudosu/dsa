def sort(arr):
    if len(arr) == 0:
        return arr

    pivot = arr[-1]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return sort(left) + middle + sort(right)


def findMedianSortedArrays(nums1, nums2):
    # merge the array
    # sort the array
    # check len of array for even and odd to find the middle element/'s
    # calculate the medium

    arr = nums1 + nums2  # merge
    # sorting
    s_arr = sort(arr)

    l = len(arr)
    if l % 2 == 0:
        a = l // 2
        b = a - 1
        return (s_arr[a] + s_arr[b]) / 2
    else:
        a = l // 2
        return s_arr[a]


num1 = [1, 2]
num2 = [3, 4]

result = findMedianSortedArrays(nums1=num1, nums2=num2)
print(result)
