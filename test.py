def getLongestSubarray(a: [int], k: int) -> int:
    n = len(a) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += a[i]
        if Sum not in preSumMap:
            preSumMap[Sum] = i

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        # if Sum not in preSumMap:
        #     preSumMap[Sum] = i

    return maxLen


arr1 = [1, 1, 2, 0, -1, -1, 3, ]
print(getLongestSubarray(a=arr1, k=3))
