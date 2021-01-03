class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = ""
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j + 1 <= 3 or dp[i - 1][j + 1]):
                    dp[i][j] = 1
                    res = max(res, s[j : i + 1], key=len)
        return res

        

