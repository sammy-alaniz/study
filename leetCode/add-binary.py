'''
Given two binary strings a and b, return their sum as a binary string.

Example 1

Input: a = "11", b = "1"
Output: "100"

Example 2

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


'''
# did not get this
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # pop off right most char
        # add
        # if 0 append 0
        # if 1 append 0
        # if 2 append 0, carry 1
        # if 3 append 1, carry 1
        # if nothing left, add carry if we have a carry

        # 0 dec = 0 bin
        # 1 dec = 1 bin
        # 2 dec = 10 bin
        # 3 dec = 11 bin

        what_to_add = { 0:('0',0) , 1:('1', 0) , 2:('0', 1) , 3:('1', 1) }

        carry = 0
        output = ""
        iterate = max(len(a), len(b))

        for i in range(iterate-1, -1, -1):
            if i == -1:
                break
            idx = i

            if idx > len(a)-1:
                bin_a = 0
            else:
                bin_a = int(a[-i])

            if idx > len(b)-1:
                bin_b = 0
            else:
                bin_b = int(b[-1])

            itr_add = carry + bin_a + bin_a

            char_to_add, carry = what_to_add[itr_add]

            output += char_to_add

        return output

if __name__ == "__main__":
    print('add binary')
