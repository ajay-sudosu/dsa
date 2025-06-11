"""
Pending questions:
- Next Permutation
"""


def two_sum_op(arr, k):
    save = {}

    for i in arr:
        rem = k - i
        if i in save:
            return [i, save[i]]
        else:
            save[rem] = i


check0 = [1, 2, 3, 4, 5, 7]
# print(two_sum_op(arr=check0, k=9))


def two_sum(arr, k):
    """
    O(n^2)
    """
    for i in arr:
        for j in range(1, len(arr)):
            if i + arr[j] == k:
                return [i, arr[j]]


check1 = [1, 1, 3, 4, 5, 7]
# print(two_sum(arr=check1, k=9))


def sort0_1_2(arr):
    """
        Dutch National flag algo
    """
    mid = 0
    left = 0
    right = len(arr) - 1

    while mid <= right:  # mid is checked for <= because of last element to process, try with (arr = [0,1, 2])
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            mid += 1
            left += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1
    return arr


check2 = [0, 1, 2, 1, 0, 2, 0, 1]
# print(sort0_1_2(arr=check2))


def majority_element(arr):
    save = {}
    n = len(arr) // 2
    element = arr[0]
    max_num = 0
    for i in arr:
        if i in save:
            save[i] += 1
            max_num = max(save[i], max_num)
        else:
            save[i] = 1
    for i, j in save.items():
        if j > n:
            element = i
            break
    return element


check3 = [3, 4, 5, 5, 1, 1, 1, 1, 1]
# print(majority_element(arr=check3))


def majority_element_moores_voting_algo(arr, n):
    # if the question states that the array has majority element that is present greater than n // 2 times
    element = None
    count = 0

    for i in arr:
        if count == 0:
            element = i
            count += 1

        elif i == element:
            count += 1

        else:
            count -= 1

    # if question does not guarantee majority element is present it could be None below is the another check
    # Checking if the stored element is the majority element
    check = 0
    for i in arr:
        if i == element:
            check += 1

    if check > (n / 2):
        return element
    return -1


check4 = [3, 4, 5, ]
# print(majority_element_moores_voting_algo(check4, n=4))


def maximum_subarray_sum(arr):
    """
    This is a brute force approach
    """
    max_sum = arr[0]
    for i in range(len(arr)):
        sub_total = 0
        for j in range(i, len(arr)):
            sub_total = sub_total + arr[j]
            max_sum = max(max_sum, sub_total)
    return max_sum


check5 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maximum_subarray_sum(arr=check5))


def maximum_subarray_sum_kandane_algo_1(arr):
    max_sum = sub_total = arr[0]

    for i in arr[1:]:
        sub_total = max(i, sub_total+i)
        max_sum = max(sub_total, max_sum)
    return max_sum


check6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maximum_subarray_sum_kandane_algo_1(arr=check6))


def maximum_subarray_sum_kandane_algo_2(arr):
    max_sum = sub_total = arr[0]

    for i in arr:
        sub_total += i
        if sub_total > max_sum:
            max_sum = sub_total
        if sub_total < 0:
            sub_total = 0

    return max_sum


check7 = [-2, -1, -2]
# print(maximum_subarray_sum_kandane_algo_2(arr=check7))


def maximum_subarray_sum_with_subarry(arr):
    max_sum = arr[0]
    sub_total = 0
    start = 0
    end = -1
    begin = -1
    for i in range(len(arr)):
        if sub_total == 0:
            start = i
        sub_total += arr[i]
        if sub_total > max_sum:
            max_sum = sub_total
            begin = start
            end = i
        if sub_total < 0:
            sub_total = 0

    return arr[begin: end+1], max_sum


# check8 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr1 = [5, -4, -2, 1, 2, -1, -2, 6]

# check8 = [-2, ]
# print(maximum_subarray_sum_with_subarry(arr1))


def buy_and_sell(arr):
    minimum = float("inf")
    max_sum = 0
    for i in arr:
        minimum = min(i, minimum)
        max_sum = max(max_sum, i-minimum)
    return max_sum


# check9 = [7, 1, 5, 3, 6, 4]
check9 = [3, 8, 2, 5, 1, 7]
# print(buy_and_sell(check9))


def arrange_array_element_by_sign(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    result = []
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result


check10 = [1, -1, 2, -3]
# print(arrange_array_element_by_sign(check10))


def arrange_array_element_by_sign_optimized(arr):
    pos_index = 0
    neg_index = 1
    result = [0] * len(arr)

    for i in range(len(arr)):
        if arr[i] > 0:
            result[pos_index] = arr[i]
            pos_index += 2
        else:
            result[neg_index] = arr[i]
            neg_index += 2
    return result


check11 = [-7, 8, 1, -1, 2, -3]
# print(arrange_array_element_by_sign_optimized(check11))


def arrange_array_element_by_sign_unequal_optimized(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    count = 0
    arr_index = 0
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[i * 2] = pos[i]
            arr[2 * i + 1] = neg[i]
            arr_index += 1
            count += 1

        count = count*2
        for i in pos[arr_index:]:
            arr[count] = i
            count += 1

    else:
        for i in range(len(pos)):
            arr[i * 2] = pos[i]
            arr[2 * i + 1] = neg[i]
            arr_index += 1
            count += 1

        count = count * 2
        for i in neg[arr_index:]:
            arr[count] = i
            count += 1
    return arr


check12 = [-7, 1, 3, 4, 5]
# print(arrange_array_element_by_sign_unequal_optimized(check12))


def leader_of_array_brute_force(arr):
    result = []
    for i in range(len(arr)):

        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                break
        else:
            result.append(arr[i])
    return result


check13 = [10]
# print(leader_of_array_brute_force(check13))


def leader_of_array_optimal(arr):
    max_num = arr[-1]
    result = [max_num]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > max_num:
            result.append(arr[i])
            max_num = arr[i]
    return result


# check14 = [10, 22, 12, 3, 0, 6]
check14 = [4, 7, 1, 0]
# print(leader_of_array_optimal(check14))


def helper_consecutive_seq(arr, num):
    for i in arr:
        if i == num:
            return True
    return False


def consecutive_seq_brute_force(arr):
    seq_count = 1

    for i in range(len(arr)):
        num = arr[i]
        count = 1
        while helper_consecutive_seq(arr, num+1):
            num += 1
            count += 1
        seq_count = max(seq_count, count)
    return seq_count


check15 = [4, 7, 1, 3, 2]
# print(consecutive_seq_brute_force(check15))


def consecutive_seq_optimal(arr):
    max_count = 1
    last_min = float("-inf")
    count = 0
    arr.sort()
    for i in range(len(arr)):
        if arr[i] - 1 == last_min:
            last_min = arr[i]
            count += 1

        elif arr[i] != last_min:
            count = 1
            last_min = arr[i]
        max_count = max(max_count, count)

    return max_count


check16 = [4, 7, 1, 1, 1, 3, 2, 5]
print(consecutive_seq_optimal(check16))
