# my original solution
# way off

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        pali = []

        for char in s:
            if len(pali) == 0:
                pali.append(char)
            elif pali[-1] != char:
                pali.append(char)
            else:
                pali.clear()
                pali.append(char)

            tmp_one = ""
            for letter_one in pali:
                tmp_one += letter_one

            tmp_two = tmp_one[::-1]

            if tmp_one == tmp_two:
                if count < len(tmp_one):
                    count = len(tmp_one)
        
        return count

class RealSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start,end):
            chars = set()
            for i in range(start, end+1):
                c = s[i]
                if c in chars:
                    return False
                chars.add(c)
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i,n):
                if check(i,j):
                    res = max(res, j - i + 1)
        
        return res

if __name__ == "__main__":
    rs = RealSolution()
    num = rs.lengthOfLongestSubstring("abcabcbb")
    print(str(num))