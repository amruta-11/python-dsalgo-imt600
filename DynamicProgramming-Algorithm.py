# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return(1)
        elif n == 2:
            return(2)
        else:
            steps = [0] * n
            steps[0] = 1
            steps[1] = 2

            # Below we are creating an array that will store the results from the previous steps to caluclate final step. This is called memoization.
            for i in range(2, n):
                steps[i] = steps[i-1] + steps[i-2]

            return(steps[n-1])