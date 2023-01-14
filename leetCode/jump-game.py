'''
https://leetcode.com/problems/jump-game/solutions/


'''

#My attempt, didn't work.
class Solution:
    def sammy_jump(self, nums: List[int], current_index: int, next_index: int) -> bool:

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

    def sammy_canJump(self, nums: List[int]) -> bool:
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

# approach_one_canJump & approach_one_canJumpFromPosition are from the problem solution
    def approach_one_canJumpFromPosition(self, position: int, nums: List[int]) -> bool:
        if position == (len(nums) - 1):
            return True

        furthestJump = min( (position + nums[position]) , (len(nums) - 1) )

        nextPosition = position + 1

        while nextPosition <= furthestJump:
            if self.canJumpFromPosition(nextPosition, nums):
                return True
            nextPosition += 1

        return False
    
    def approach_one_canJump(self, nums: List[int]) -> bool:
        return self.approach_one_canJumpFromPosition(0, nums)


