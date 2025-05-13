from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            width = end - start
            h = min(height[start], height[end])
            curr_area = h * width
            area = max(area, curr_area)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return area


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# arr = [4, 3, 2, 1, 4]

s = Solution()
print(s.maxArea(height=arr))
