# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            i = TreeNode(preorder.pop(0))
            idx = inorder.index(i.val)
            i.left = self.buildTree(preorder, inorder[:idx])
            i.right = self.buildTree(preorder, inorder[idx+1:])
            return i

