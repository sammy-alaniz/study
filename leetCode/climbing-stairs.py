'''my original attempt'''
from collections import deque
import time

class originalAttempt:
    def climbStairs(self, n: int) -> int:
        distinct_ways = [[]]


        # start with inital variation, C1 x number of stairs = number of stairs
        for _ in range(n):
            distinct_ways[0].append(1)

        latest_iteration = distinct_ways[0]

        while latest_iteration.count(1) >= 2 and (len(latest_iteration) > 1):

              dq = deque(latest_iteration)

              one = dq.pop()
              two = dq.pop()

              if (one == 1) == (two == 1):
                  dq.append(2)
                  latest_iteration = list(dq)
                  distinct_ways.append(latest_iteration)

              elif (one == 2) and (two == 1):
                  dq.append(2)
                  dq.append(1)
                  latest_iteration = list(dq)
                  distinct_ways.append(latest_iteration)
              elif (one == 1) and (two == 2):
                   dq.append(1)
                   dq.appendleft(2)
                   latest_iteration = list(dq)
                   distinct_ways.append(latest_iteration)


            


        return len(distinct_ways)

'''second attempt'''
class Solution:
    def climbStairs(self, n: int) -> int:
        distinct_ways = [[]]
        # start with inital variation, C1 x number of stairs = number of stairs
        for _ in range(n):
            distinct_ways[0].append(1)

        latest_iteration = distinct_ways[0]

        while latest_iteration.count(1) >= 2 and (len(latest_iteration) > 1):

              dq = deque(latest_iteration)

              one = dq.pop()
              two = dq.pop()

              if (one == 1) == (two == 1):
                  dq.appendleft(2)
                  latest_iteration = list(dq)
                  distinct_ways.append(latest_iteration)

              elif (one == 2) and (two == 1):
                  dq.append(2)
                  dq.append(1)
                  latest_iteration = list(dq)
                  distinct_ways.append(latest_iteration)
        
        final_list = []

        count = 0

        for way in distinct_ways:
            if way.count(1) == len(way):
                count += 1
                continue
            if way.count(2) == len(way):
                count += 1
                continue

            print(str(way.count(1)))
            
            if way.count(1) > way.count(2):
                count = count + way.count(1) + 1
            elif way.count(1) < way.count(2):
                count = count + way.count(2) + 1
            elif way.count(1) == way.count(2):
                count = count + 1
            



        return count

'''this works for 44 test cases'''
class SolutionMemMax(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def climb(n):
            if n==1: #only one step option is availble
                time.sleep(0.1)
                return 1
            if n ==2: # two options are possible : to take two 1-stpes or to only take one 2-steps
                time.sleep(0.2)
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)

    def climb_dp(self, n):
        #edge cases
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]
		
# how is th dp version working

if __name__ == "__main__":
    sol = SolutionMemMax()
    num = sol.climb_dp(44)
    #1,134,903,170
    print(str(num))