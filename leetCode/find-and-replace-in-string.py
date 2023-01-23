'''
Link : https://leetcode.com/problems/find-and-replace-in-string/

You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

Example 1:

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Example  2

Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.

Constraints:

1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indexes[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.

'''

# mine, didn't work, miss understood that target doesn't always start with zero
# this version doesn't work, but one did for targets at zero
# scraped solution when I noticed I was off

# 1 - check if 's' at specified 'indices' contain chars in 'sources'
# 2 - 
# ------
# 1 - for loop through length of 'indicies'
# 2 - find starting index, and length of 'sources' string to include in change
# 3 - based on the found location, does it equal the starting point from indices
# 4 - if so append 'targets' to a return array structure
# 5 - find chars that aren't included in the 'changed' chars and append to retrun array structure

class Not_Work_Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        rtn_arrary = []

        for i in range(len(indices)):
            print('\nIteration ', i)
            starting_indice = indices[i]
            must_have = sources[i]
            new_substring = targets[i]
            #print('where the indicie should be : ', starting_indice)
            print('source : ', must_have)
            print('target : ', new_substring)

            searchable_string = s[starting_indice:]
            print('searchable_string : ', searchable_string)

            found_substring_index = searchable_string.find(must_have)
            print('Found = 0 - Not Found = -1 : ', found_substring_index)

            if i == len(indices)-1:
                sub_str_orig = s[indices[i]:]
            elif i ==0:
                sub_str_orig = s[:indices[i]]
            else:
                sub_str_orig = s[indices[i]:indices[i+1]]

            print('original substring : ', sub_str_orig)

            if found_substring_index == 0 :
                rtn_arrary.append(new_substring)
                print('source found and target appended' , rtn_arrary)

            if found_substring_index == 0 and len(must_have) < len(sub_str_orig):
                start = len(must_have) 
                end = len(sub_str_orig)
                missed_substring = searchable_string[start:end]
                rtn_arrary.append(missed_substring)
                print('target did not completely match original string', rtn_arrary)

            if found_substring_index == -1:
                print('substring from source was not found at correct indicie')
                rtn_arrary.append(sub_str_orig)

            print(rtn_arrary)
        
        print('rtn_array after for loop', rtn_arrary)
        rtn_str = ""
        for substring in rtn_arrary:
            rtn_str += substring

        return rtn_str

# this worked! I didn't understand that my inputs weren't sorted, and didnt account I could have matches later down in the string
class Solution:

    def re_order_inputs(self, indicies:list[int], sources:list[int], targets:list[int]):
        original_indicies = []
        original_sources = []
        original_targets = []

        for i in range(len(indicies)):
            original_indicies.append(indicies[i])
            original_sources.append(sources[i])
            original_targets.append(targets[i])

        indicies.sort()

        for i in range(len(indicies)):
            index = original_indicies.index(indicies[i])
            sources[i] = original_sources[index]
            targets[i] = original_targets[index]


    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        self.re_order_inputs(indices,sources,targets)

        rtn_arrary = []

        for i in range(len(indices)):
            print('\nIteration ', i)
            starting_indice = indices[i]
            must_have = sources[i]
            new_substring = targets[i]
            #print('where the indicie should be : ', starting_indice)
            print('source : ', must_have)
            print('target : ', new_substring)

            searchable_string = s[starting_indice:]
            print('searchable_string : ', searchable_string)

            found_substring_index = searchable_string.find(must_have)
            print('Found = 0 - Not Found = -1 : ', found_substring_index)

            if i == len(indices)-1:
                sub_str_orig = s[indices[i]:]
            else:
                sub_str_orig = s[indices[i]:indices[i+1]]

            print('original substring : ', sub_str_orig)

            if found_substring_index == 0 :
                rtn_arrary.append(new_substring)
                print('source found and target appended' , rtn_arrary)

            if found_substring_index == 0 and len(must_have) < len(sub_str_orig):
                start = len(must_have) 
                end = len(sub_str_orig)
                missed_substring = searchable_string[start:end]
                rtn_arrary.append(missed_substring)
                print('target did not completely match original string', rtn_arrary)

            if found_substring_index != 0:
                print('substring from source was not found at correct indicie')
                rtn_arrary.append(sub_str_orig)

            print(rtn_arrary)

        if indices[0] != 0:
            tmp = s[:indices[0]]
            rtn_arrary.insert(0, s[:indices[0]])
        
        print('rtn_array after for loop', rtn_arrary)
        rtn_str = ""
        for substring in rtn_arrary:
            rtn_str += substring

        return rtn_str



