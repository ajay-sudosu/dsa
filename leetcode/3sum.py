from typing import List


class Solution:
    """
    Brute force solution to find the result (Time limit exceeded for large set of data)
    """
    def three_sum_brute_force(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()

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


arr = [-2, 0, 1, 1, 2]


# s = Solution()
# print(s.three_sum_brute_force(nums=arr))


