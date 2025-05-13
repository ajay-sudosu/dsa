from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}
    o = []
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [d[diff], i]
        d[nums[i]] = i


result = twoSum(nums=[-3, 4, 3, 90], target=0)
print(result)
