''''
Link : https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105


'''

# Mine almost totalyy worked! 321/322 test cases passes, On^2
# 1 - edge case for element zero, it can't look to the left
# 2 - edge case for element n-1, it can't loot to the right
# 3 - at element x, look left for an element greater than x
# 3 - at element x, look right for an element greater than x
# 4 - element found left of x index (left_x_index) and right of x index (right_x_index)
# 5 - min(value(left_x_index), value(right_x_index)) - value(x_index) * (right_x_index - left_x_index)

# ------
# 1 - 

# 1 - edge case for element zero, it can't look to the left
# 2 - edge case for element n-1, it can't loot to the right
# 3 - at element x, look left for largest element
# 4 - at element x, look right for largest element
# 5 - min(value(left_largest_index), value(right_largest_index)) - value(x_index) 


class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        for i in range(len(height)-1):
            
            # if first or last element, skip
            if i == 0 or i == len(height)-1:
                continue
            
            left_largest = max(height[:i])
            right_largest = max(height[i:])

            if left_largest <= height[i] or right_largest <= height[i]:
                continue

            height_of_water = min(left_largest, right_largest) - height[i]

            total_water += height_of_water

        return total_water


class ChatGPT_Convert_Java_To_Python_Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans
