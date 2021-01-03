class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        for i, key in enumerate(s):
            if c[key] == 1:
                return i
        return -1
