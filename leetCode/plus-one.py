'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

'''

class Solution:
    def doesnt_work_plusOne(self, digits: list[int]) -> list[int]:
        # add one to right most digit
        # if digit adds up to greater than 9
        # replace to 9 
        # and add 1 to digit to left

        first_digit_added = False
        carry = 1

        for i in range(len(digits)-1,0,-1):

            if first_digit_added != True:
                first_digit_added = True
                digits[i] += 1
                carry = 0
                if digits[i] > 9:
                    digits[i] = 9
                    carry = 1

            if carry != 0:
                digits[i] += 1
                carry = 0
                if digits[i] > 9:
                    digits[i] = 9
                    carry = 1

        if carry == 1:
            digits[0] = 0
            digits.insert(0, 1)

        return digits

        # THIS WORKED, GOT THIS MYSELF
    def plusOne(self, digits: List[int]) -> List[int]:
        # add one to right most digit
        # if digit adds up to greater than 9
        # replace to 9 
        # and add 1 to digit to left

        carry = 0

        for i in range(len(digits)-1, -1, -1):
            # did this to also compute at index 0
            if i == -1:
                break
            
            # add one to the index i
            digits[i] += 1

            # if adding at index i made i greater than 9
            if digits[i] > 9:
                # note that we need to cary one to the next digit to the left
                carry = 1
                # keep only the ones digit
                digits[i] = digits[i] % 10
            else:
                # if adding did not make index i greater than 9, we note carry is zero and break the loop.
                # we're only adding one
                carry = 0
                break
                
        # this is for the use case that we have a carry over at the left most digit
        # make 0th digit 0
        # add 1 to the left most elements
        if carry == 1:
            digits[0] = 0
            digits.insert(0,1)

        return digits

if __name__ == "__main__":
    print('plus one')