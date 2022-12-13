# v1
#        count = 0
#        pali = []
#
#        for char in s:
#            if len(pali) == 0:
#                pali.append(char)
#            elif pali[-1] != char:
#                pali.append(char)
#            else:
#                pali.clear()
#                pali.append(char)
#
#            tmp_one = ""
#            for letter_one in pali:
#                tmp_one += letter_one
#
#            tmp_two = tmp_one[::-1]
#
#            if tmp_one == tmp_two:
#                if count < len(tmp_one):
#                    count = len(tmp_one)
#        
#        return count

# v2
# kinda worked, stopped working at test case 47 took to long
class Solution:
    def longestPalindrome_vTwo(self, s: str) -> str:
        count = 0
        longest_string = ""
        pali = []

        while len(s) > 0:
            for char in s:
                if len(pali) == 0:
                    pali.append(char)
                else:
                    pali.append(char)

                tmp_one = ""
                for letter_one in pali:
                    tmp_one += letter_one

                tmp_two = tmp_one[::-1]

                if tmp_one == tmp_two:
                    if count < len(tmp_one):
                        count = len(tmp_one)
                        longest_string = tmp_one
            pali.clear()
            s = s[1:]
        
        return longest_string

    