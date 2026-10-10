class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        #base case 1 (all single letters are palindromes)
        for i in range(n):
            dp[i][i] = True

        #Base case 2: check all the different pairs (neighbours can be palindromes)

        for i in range(n - 1):
            #n - 1 cause we can't start at the last letter ever
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                start = i
                max_len = 2


        #Step 3: The bottom up implementation for DP

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    if length > max_len:
                        max_len = length
                        start = i
    
        return s[start:start + max_len]

        
            