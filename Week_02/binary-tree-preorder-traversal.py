# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        # Recursion Method
        '''
        def pre(root):
            if root:
                res.append(root.val)
                pre(root.left)
                pre(root.right)
        pre(root)        
        '''
        # Iteration Method
        if root == None:
            return []
        stack = [root]
        t = type(root)
        while stack:
            tmp = stack.pop()
            if type(tmp) != t and tmp != None:
                res.append(tmp)
                continue
            if tmp:
                stack.append(tmp.right)
                stack.append(tmp.left)
                stack.append(tmp.val)
        return res
