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
class Solution:

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

