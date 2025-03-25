def twoSum(nums, target):
    saves = {}
    for i in range(len(nums)):
        x = target - nums[i]
        if x in saves:
            return [i, saves[x]]
        saves[nums[i]] = i

# print(twoSum(nums=[2, 5, 5, 11], target=10))
print(twoSum(nums=[3, 2, 4], target=6))
