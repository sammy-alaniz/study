'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

'''


class Solution:
    # i got close
    def threeSum_mine(self, nums: list[int]) -> list[list[int]]:
        output = []
        dup_check = []
        for i in nums:
            for j in nums:
                if i == j:
                    continue
                for k in nums:
                    if i == k or j == k:
                        continue
                    tmp = [i,j,k]
                    tmp.sort()
                    if 0 == (i + j + k) and \
                       [i,j,k] not in output and \
                       tmp not in dup_check:
                       output.append([i,j,k])
                       dup_check.append(tmp)

        return output

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: list[int], i: int, res:list[list[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]

            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                lo -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1