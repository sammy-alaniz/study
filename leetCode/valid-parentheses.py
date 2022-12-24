'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true


Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

'''
from collections import deque

class Solution:

    def check_open_close(self, left: str, right:str) -> bool:
        if right == '}' and left == '{':
            return True
        elif right == ')' and left == '(':
            return True
        elif right == ']' and left == '[':
            return True
        else:
            return False


    def isValid(self, s: str) -> bool:
        dq = deque()

        if s.count('[') != s.count(']'):
            return False
        elif s.count('(') != s.count(')'):
            return False
        elif s.count('{') != s.count('}'):
            return False

        for i in range(len(s)):
            if s[i] == ')' or s[i] == ' }' or s[i] == ']':
                if i != 0 and self.check_open_close(s[i-1], s[i]):
                    break
                else:
                    return False
            else:
                dq.append(s[i])

        while dq:
            next = dq.pop()

            for i in range(len(s)):
                if s[i] != ')' or s[i] != ' }' or s[i] != ']':
                    continue
                elif s[i] == next:
                    continue
                else:
                    return False

        return True

    def correct_isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


if __name__ == "__main__":
    sol = Solution()
    tf = sol.isValid([])

    print(str(tf))