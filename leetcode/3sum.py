from typing import List


class Solution:
    """
    Brute force solution to find the result (Time limit exceeded for large set of data)
    """
    def three_sum_brute_force(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for i in range(len(nums)):
            curr = nums[i]
            a1 = i+1
            a2 = i+2

            while a2 <= len(nums) - 1:
                second = nums[a1]
                third = a2
                while third <= len(nums) - 1:
                    if curr + second + nums[third] == 0:
                        if [curr, second, nums[third]] not in result:
                            result.append([curr, second, nums[third]])
                        third += 1
                    else:
                        third += 1
                a1 += 1
                a2 += 1
        return result


arr = [-1,0,1,2,-1,-4]
# arr = [0,1,1]


# s = Solution()
# print(s.three_sum_brute_force(nums=arr))


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()

    result = []

    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i+1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right] + nums[i]
            if curr_sum < 0:
                left += 1
            elif curr_sum > 0:
                right -= 1
            else:
                result.append([nums[left], nums[right], nums[i]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


print(three_sum(nums=arr))
