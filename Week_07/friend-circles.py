class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ans = n = len(M)
        p = [*range(n)]
        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]
        for i, j in itertools.combinations(range(n), 2):
            if M[i][j] and (pi := f(i)) != (pj := f(j)):
                p[pi] = pj
                ans -= 1
        return ans
