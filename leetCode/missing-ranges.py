'''
Link: https://leetcode.com/problems/missing-ranges/description/

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.

Constraints:
-109 <= lower <= upper <= 109
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.


'''
# got this after watching video explaining a solution, but wrote on my own
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        missing_ranges = []
        adjusted_lower = lower - 1
        adjusted_upper = upper + 1

        nums.insert(0, adjusted_lower)
        nums.append(adjusted_upper)

        for i in range(len(nums)-1):
            if i == len(nums):
                break
            
            a = nums[i] + 1
            b = nums[i+1] - 1

            if a < b:
                missing_ranges.append(str(a) + "->" + str(b))
            elif a == b:
                missing_ranges.append(str(a))

        return missing_ranges
