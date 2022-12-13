class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for ai in range(len(nums)):
            for bi in range(len(nums)):
                if ai == bi:
                    continue
                elif (nums[ai]+nums[bi]) == target:
                    return [ai,bi]

if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    tar = 9
    ab = []
    ab = sol.twoSum(numbers,tar)
    print(str(ab))

    # whoop got this one on my own