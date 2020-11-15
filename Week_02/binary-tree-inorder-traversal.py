# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        # Recursion
        '''
        def ino(root):
            if root:
                ino(root.left)
                res.append(root.val)
                ino(root.right)
        ino(root)
        return res
        '''

        # Iteration
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
                stack.append(tmp.val)
                stack.append(tmp.left)
        return res
