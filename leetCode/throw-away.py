from sortedcontainers import SortedList

K_ODD, K_EVEN = 0, 1


def oddEvenJumps(self, arr: List[int]) -> int:
    n = len(arr)
    sorted_nums, nums_idx = SortedList([arr[-1]]), {arr[-1]: n - 1}
    dp = [[False, False] for _ in range(n)]
    dp[n - 1] = [True, True]

    # Time: O(n)
    for i in range(n - 2, -1, -1):
        num = arr[i]

        # Time: O(logn)
        idx = sorted_nums.bisect_left(num)

        if idx < len(sorted_nums) and sorted_nums[idx] >= num:
            dp[i][K_ODD] = dp[nums_idx[sorted_nums[idx]]][K_EVEN]

        if idx < len(sorted_nums) and sorted_nums[idx] == num:
            dp[i][K_EVEN] = dp[nums_idx[sorted_nums[idx]]][K_ODD]
        elif idx > 0:
            dp[i][K_EVEN] = dp[nums_idx[sorted_nums[idx - 1]]][K_ODD]

        # Time: O(logn)
        if idx == len(sorted_nums) or sorted_nums[idx] != num:
            sorted_nums.add(num)
        nums_idx[num] = i

    return sum(odd for odd, even in dp)

print(oddEvenJumps([10,13,12,14,15]))



