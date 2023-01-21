'''
Link : https://leetcode.com/problems/next-closest-time/description/

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

Constraints:

time.length == 5
time is a valid time in the form "HH:MM".
0 <= HH < 24
0 <= MM < 60


'''
# I got this one!
class Solution:
    def convertToArray(self, time:str) -> list[int]:
        print('convertToArray Input : ', time)
        converted_time = []
        for char in time:
            if char == ':' :
                continue
            converted_time.append(int(char))
        print('convertToArray Output : ', converted_time)
        return converted_time

    def convertToString(self, time:list[int]) -> str:
        print('convertingToString Input : ', time)
        converted_time = ""
        for i in range(len(time)):
            converted_time += str(time[i])
        rtn_val = converted_time[:2] + ':' + converted_time[2:]
        print('convertingToString Output : ', rtn_val)
        return rtn_val

    def validTime(self, original_time:list[int], proposed_time:list[int]) -> bool:
        print('validTime Inputs - Original Time: ', original_time, 'Proposed Time', proposed_time)
        digit_one = proposed_time[0]
        digit_two = proposed_time[1]
        proposed_hours = str(digit_one) + str(digit_two)
        print('proposed hours : ', proposed_hours)

        digit_two = proposed_time[2]
        digit_three = proposed_time[3]
        proposed_minutes = str(digit_two) + str(digit_three)
        print('proposed minutes : ', proposed_minutes)

        if int(proposed_hours) >= 24:
            print('proposed hour time invalid')
            return False

        if int(proposed_minutes) >= 60:
            print('proposed minute time invalid')
            return False

        print('proposed time is valid')

        original_digit_one = original_time[0]
        original_digit_two = original_time[1]
        original_digit_three = original_time[2]
        original_digit_four = original_time[3]

        original_hours = str(original_digit_one) + str(original_digit_two)
        original_minutes = str(original_digit_three) + str(original_digit_four)
        print('original hours : ', original_hours)
        print('original minutes : ', original_minutes)

        if int(proposed_hours) < int(original_hours):
            print('proposed hours was less than original hours')
            return False

        if int(proposed_hours) == int(original_hours) and int(proposed_minutes) <= int(original_minutes):
            print('proposed and original had equal hours, but proposed minutes was less or equal to than original minutes')
            return False
        
        print('proposed time was valid and less than original value')
        return True


    def nextClosestTime(self, time: str) -> str:

        unique_values = []

        # find unique values
        for char in time:
            if char == ':':
                continue
            if int(char) not in unique_values:
                unique_values.append(int(char))

        unique_values.sort()
        print('unique values sorted : ', unique_values)

        original_time = []

        original_time = self.convertToArray(time)
        proposed_time = self.convertToArray(time)

        print('before loop print')
        
        # range(start, stop, step)
        for a in range(len(original_time)-1, -1, -1):
            print('a : ', a)
            for b in range(len(unique_values)):
                print('b : ', b)
                proposed_time[a] = unique_values[b]
                if self.validTime(original_time, proposed_time):
                    return self.convertToString(proposed_time)
            proposed_time[a] = min(unique_values)

        smallest_value = min(unique_values)
        
        last_resort = []

        for i in range(4):
            last_resort.append(smallest_value)

        return self.convertToString(last_resort)