"""
    findMedianSortedArrays is my first approach
"""


def sort(arr):
    if len(arr) == 0:
        return arr

    pivot = arr[-1]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return sort(left) + middle + sort(right)


def find_median_sorted_arrays(nums1, nums2):
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


# test case
num1 = [1, 3]
num2 = [2]

# result = find_median_sorted_arrays(nums1=num1, nums2=num2)
# print(result)


"""
This is a better approach 
"""


def find_median_sorted_arrays_better(nums1, nums2):
        left = 0
        right = 0
        s_arr = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                s_arr.append(nums1[left])
                left += 1
            else:
                s_arr.append(nums2[right])
                right += 1
        s_arr = s_arr + nums1[left:] + nums2[right:]

        l = len(s_arr)
        if l % 2 == 0:
            a = l // 2
            b = a - 1
            return (s_arr[a] + s_arr[b]) / 2
        else:
            a = l // 2
            return s_arr[a]


result = find_median_sorted_arrays_better(nums1=num1, nums2=num2)
print(result)
