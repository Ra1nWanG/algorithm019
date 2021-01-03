class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.strip()
        left, right = len(s) - 1, len(s) - 1
        while left >= 0:
            while left >= 0 and s[left] != " ":
                left -= 1
            res.append(s[left + 1: right + 1])
            while s[left] == " ":
                left -= 1
            right = left
        return " ".join(res)
