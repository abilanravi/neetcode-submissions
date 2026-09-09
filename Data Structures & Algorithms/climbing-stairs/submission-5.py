class Solution:
    def climbStairs(self, n: int) -> int:
        
        one, two = 2, 1

        if n == 1:
            return 1
        if n == 2:
            return 2

        for i in range(3, n+1):
            current = one + two
            two, one = one, current

        return one

