"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Iteration with deque
        '''
        from collections import deque
        if root == None:
            return []
        stack = deque([root])
        res = []
        while stack:
            level = []
            for i in range(len(stack)):
                tmp = stack.popleft()
                level.append(tmp.val)
                stack.extend(tmp.children)
            res.append(level)
        return res
        '''
        # Recursion Method
        res = []
        def helper(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                helper(child, level + 1)
        
        if root:
            helper(root, 0)
        return res
