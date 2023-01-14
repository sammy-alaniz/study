'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Example 1
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()

        ans = False

        for ia in range(len(nums)):
            for ib in range(ia+1, len(nums)):
                if nums[ia] > nums[ib]:
                    tmp_ia = nums[ia]
                    tmp_ib = nums[ib]

                    nums[ia] = tmp_ib
                    nums[ib] = tmp_ia
                    nums[:ib] = sorted(nums[:ib], reverse=True)
                    nums.reverse()
                    ans = True
                    break
            if ans:
                break 

    def Attempt_two_nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()

        ans = False

        for ia in range(len(nums)):
            for ib in range(ia+1, len(nums)):
                if nums[ia] > nums[ib]: # and ib == (ia + 1):
                    tmp_ia = nums[ia]
                    tmp_ib = nums[ib]

                    nums[ia] = tmp_ib
                    nums[ib] = tmp_ia
                    nums[:ib] = sorted(nums[:ib], reverse=True)
                    nums.reverse()
                    ans = True
                    break
            if ans:
                break

    def correct_answer_nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i - 1] < nums[i]:
                nums[i:] = sorted(nums[i:])

                j = i - 1

                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums

        return nums.reverse()
if __name__ == "__main__":
    pirnt('next permutation')