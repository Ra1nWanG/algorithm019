class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        l1, l2 = len(arr1), len(arr2)
        if l1 * l2 == 0:
            return []
        c = Counter(arr1)
        res = []
        for n in arr2:
            while c.get(n):
                c[n] -= 1
                res.append(n)
            c.pop(n)
        return res + sorted(list(c.elements()))
