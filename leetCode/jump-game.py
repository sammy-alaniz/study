'''
https://leetcode.com/problems/jump-game/solutions/


'''

#My attempt, didn't work.
class Solution:
    def sammy_jump(self, nums: list[int], current_index: int, next_index: int) -> bool:

       last_index = len(nums) - 1

       if next_index == last_index :
           return True
       elif next_index > last_index :
            return False
       elif nums[current_index] == 0:
            return False
        
       for i in range(nums[next_index]):
           if self.jump(nums, next_index, i ):
               return True
        
       return False

    def sammy_canJump(self, nums: list[int]) -> bool:
         # recursive
         # given jump(curren-index, next-index)
         # if zero return false
         # if exceedes arrau return false
         # if last index return true
 
         end_or_not = False
 
         for i in range(nums[0]):
             end_or_not = self.jump(nums, 0, i)
             if end_or_not == True:
                 return True
         return False

# approach_one_canJump & approach_one_canJumpFromPosition are from the problem solution, a.k.a. backtracking
    def approach_one_canJumpFromPosition(self, position: int, nums: list[int]) -> bool:
        if position == (len(nums) - 1):
            return True

        furthestJump = min( (position + nums[position]) , (len(nums) - 1) )

        nextPosition = position + 1

        while nextPosition <= furthestJump:
            if self.canJumpFromPosition(nextPosition, nums):
                return True
            nextPosition += 1

        return False
    
    def approach_one_canJump(self, nums: list[int]) -> bool:
        return self.approach_one_canJumpFromPosition(0, nums)

# approach two - dynamic programming top down
from enum import Enum

class Index(Enum):
    GOOD = 1
    BAD = 2
    UNKNOWN = 3

class ApproachTwoSolution:
    def __init__(self) -> None:
        self.memo = []

    def canJumpFromPosition(self, position: int, nums: list[int]) -> bool:
        if self.memo[position] != Index.UNKNOWN:
            if self.memo[position] == Index.GOOD:
                return True
            else:
                # if it isn't unkown or good, then it's bad
                return False

        if position == (len(nums) - 1):
            return True

        furthestJump = min( (position + nums[position]) , (len(nums) - 1) )

        nextPosition = position + 1

        while nextPosition <= furthestJump:
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = Index.GOOD
                return True
            nextPosition += 1

        self.memo[position] = Index.BAD
        return False

    def canJump(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            self.memo.append(Index.UNKNOWN)

        # last posistion is always good
        self.memo[len(self.memo)-1] = Index.GOOD

        return self.canJumpFromPosition(0, nums)


class APPTHREE_Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = []

        for i in range(len(nums)):
            memo.append(Index.UNKNOWN)

        # last posistion is always good
        memo[len(memo)-1] = Index.GOOD

        len_of_array = len(nums) - 2 # excldue the last index, range is non-inclusive
        stop_at = -1
        itterate_at = -1


        for i in range(len_of_array, stop_at, itterate_at):
            furthextJump = min( (i + nums[i]) , (len(nums) - 1) )

            for j in range(i+1, furthextJump+1):
                if memo[j] == Index.GOOD :
                    memo[i] == Index.GOOD
                    break

        return memo[0] == Index.GOOD

# below is a coversion from chatgpt, it went from java to python
#from enum import Enum
#
#class Index(Enum):
#    GOOD = 1
#    BAD = 2
#    UNKNOWN = 3

class CHATGPT_APPTHREE_Solution:
    def canJump(self, nums):
        memo = [Index.UNKNOWN for _ in nums]
        memo[-1] = Index.GOOD

        for i in range(len(nums)-2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i+1, furthestJump+1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break
        return memo[0] == Index.GOOD
# 1 - create array of unknown enums
# 2 - make last element of array good
# 3 - Top Loop : start from the second to last item in the array
# 4 - Top Loop : move to the left, from the second to last item in the array
# 5 - Inner Loop : take the smaller value between A) posistion plus positions element value or B) length of the array (minus one because it's not inclusive)
# 6 - Inner Loop : start at current posistion plus one and end at the smaller value
# 7 - 



if __name__ == "__main__":
    print('\nJump Game')