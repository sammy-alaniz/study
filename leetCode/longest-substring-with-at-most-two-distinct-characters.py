'''
Link : https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/


Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
Accepted
221.5K
Submissions
412.7K
Acceptance Rate
53.7%
Seen this question in a real interview before?
1/4
Yes
No
Similar Questions
Related Topics


'''



# 1 - pointer A start from left then move to the right
# 2 - pointer B start from left then move to right
# 3 - if there are two distinct characters, save off the string for that index. If not break the loop for A
# 4 - move pointer B to right and preform step 3

class Sammys_1st_attempt_Solution:

    def doesItExist(self, s: str, a:int , b:int, answers: list) -> bool:

        for i in answers:
            tmp_dict = i
            if tmp_dict['charA'] == s[a]:
                return True
        return False

    def charsMatch(self, s:str , a:int , b:int, answers: list) -> bool:

        tmp_dict = answers[a]
        charB = tmp_dict['charB']

        if charB == s[b]:
            return True
        else:
            return False

    def save(self, s:str, a:int, b:int) -> dict:
        tmp_dict = {a : { 'charA' : s[a] , 'charB' : s[b] , 'string' : s[a:b+1] } }
        return tmp_dict

    def longestString(self, answers:list) -> int:
        max = 0
        for i in range(len(answers)-1):
            element = answers[i]
            element = element[i]
            string = element['string']
            if max < len(string):
                max = len(string)

        return max

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        answers = []

        length_of_string = len(s)

        for a in range(length_of_string - 1):
            for b in range(a + 1, length_of_string - 1):

                if not self.doesItExist(s,a,b,answers):
                    answers.append(self.save(s,a,b))
                elif self.charsMatch(s,a,b,answers):
                    answers.append(self.save(s,a,b))
                else:
                    continue

        return self.longestString(answers)

# 1 - pointer A start from left then move to the right
# 2 - pointer B start from left then move to right
# 3 - if there are two distinct characters, save off the string for that index. If not break the loop for A
# 4 - move pointer B to right and preform step 3
# latest attempt, got one test case, logic is still off
class two_attempt_Solution:

    def doesItExist(self, s: str, a:int , b:int, answers: dict) -> bool:
        if a in answers:
            return True
        else:
            return False

    def charsMatch(self, s:str , a:int , b:int, answers: list) -> bool:

        tmp_dict = answers[a]
        charB = tmp_dict['charB']
        charA = tmp_dict['charA']

        tmp_sb = s[b]



        if charB == tmp_sb or charA == tmp_sb:
            return True
        else:
            return False

    def save(self, s:str, a:int, b:int) -> dict:
        tmp_dict = { 'charA' : s[a] , 'charB' : s[b] , 'string' : s[a:b+1] }
        return tmp_dict

    def longestString(self, answers:dict) -> int:
        max = 0
        for char in answers:
            element = answers[char]
            string = element['string']
            if max < len(string):
                max = len(string)
        return max

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        answers = {}

        length_of_string = len(s)

        for a in range(length_of_string - 1):
            for b in range(a + 1, length_of_string - 1):

                if not self.doesItExist(s,a,b,answers):
                    answers[a] = (self.save(s,a,b))
                elif self.charsMatch(s,a,b,answers):
                    answers[a] = (self.save(s,a,b))
                else:
                    continue

        return self.longestString(answers)


class Last_attempt_not_there_Solution:

    def doesItExist(self, s: str, a:int , b:int, answers: dict) -> bool:
        if a in answers:
            return True
        else:
            return False

    def charsMatch(self, s:str , a:int , b:int, answers: list) -> bool:

        if a not in answers:
            return False

        tmp_dict = answers[a]
        charB = tmp_dict['charB']
        charA = tmp_dict['charA']

        tmp_sb = s[b]

        if charB == tmp_sb or charA == tmp_sb:
            return True
        else:
            return False

    def save(self, s:str, a:int, b:int) -> dict:
        tmp_dict = { 'charA' : s[a] , 'charB' : s[b] , 'string' : s[a:b+1] }
        return tmp_dict

    def longestString(self, answers:dict) -> int:
        max = 0
        for char in answers:
            element = answers[char]
            string = element['string']
            if max < len(string):
                max = len(string)
        return max

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        answers = {}

        length_of_string = len(s)

        for a in range(length_of_string - 1):
            for b in range(a + 1, length_of_string):

                if not self.doesItExist(s,a,b,answers) and s[a] != s[b]:
                    answers[a] = (self.save(s,a,b))
                elif self.charsMatch(s,a,b,answers):
                    answers[a] = (self.save(s,a,b))
                else:
                    continue

        return self.longestString(answers)

# this one works, wrote on my own, but saw solution once
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_length = 0
        char_map = {}
        left_pointer = 0
        
        for right_pointer in range(len(s)):
            char = s[right_pointer]


            char_map[char] = right_pointer

            if len(char_map) == 3:
                smallest_char = min(char_map, key=char_map.get)
                smallest_index = char_map[smallest_char]
                char_map.pop(smallest_char)
                left_pointer = smallest_index + 1

            length = right_pointer - left_pointer + 1

            if length > max_length:
                max_length = length

        return max_length