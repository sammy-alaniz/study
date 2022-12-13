'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

https://leetcode.com/problems/container-with-most-water/

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        for ai in range(len(height)):
            for bi in range(ai, len(height)):
                if ai == bi:
                    continue
                min_height = min(height[ai], height[bi])
                width = abs(ai - bi)

                if area < (min_height * width):
                    area = (min_height * width)

        return area
if __name__ == "__main__":
    sol = Solution()
    area = sol.maxArea([1,8,6,2,5,4,8,3,7])

    print(str(area))