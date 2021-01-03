class Solution:
    def reverseWords(self, s: str) -> str:
        l = len(s)
        res = []
        i = 0
        while i < l:
            start = i
            while i < l and s[i] != ' ':
                i += 1
            res.append(s[start:i][::-1])
            start = i
            while i < l and s[i] == ' ':
                i += 1
            res.append(" " * (i - start))
        return "".join(res)
