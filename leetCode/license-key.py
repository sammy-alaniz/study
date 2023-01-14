'''
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.


Example 2
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Constraints:
1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 10

'''

# MINE
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        string_no_dashes = s.replace('-','')
        string_no_dashes = string_no_dashes.upper()
        length = len(string_no_dashes)

        chars_in_first_group = length % k
        print('mod', chars_in_first_group)
        number_of_dashes = length // k
        print('divide', number_of_dashes)

        lic_list = list(string_no_dashes)

        first_dash = False
        dash_count = 0

        if chars_in_first_group != 0:
            number_of_dashes += 1

        for i in range(1,number_of_dashes):
            # first dash is special
            if first_dash != True and chars_in_first_group != 0:
                first_dash = True
                lic_list.insert(chars_in_first_group,'-')
                dash_count += 1
            else:
                chars_to_skip = (i * k) + dash_count - chars_in_first_group
                lic_list.insert(chars_to_skip, '-')
                dash_count += 1

        return ''.join(str(x) for x in lic_list)

    def works_licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)):
            if(s[i] != '-'):
                ans += s[i].upper()
                count += 1
                if count == k:
                    count = 0
                    ans += '-'
        
        # remove dash at end
        if(len(ans) > 0 and ans[len(ans)-1] == '-'):
            ans = ans[:-1]
        # reverse 
        ans = ans[::-1]
        result = "".join(ans)
        return result

if __name__ == "__main__":
    