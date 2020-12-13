class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if not s or s[0] == "0":
            return 0
        dp = [1, 1] + [0] * (l - 1)
        for i in range(1, l):
            if s[i] != "0":
                dp[i + 1] += dp[i]
            if "10" <= s[i - 1 : i + 1] <= "26":
                dp[i + 1] += dp[i - 1]
        return dp[-1]
