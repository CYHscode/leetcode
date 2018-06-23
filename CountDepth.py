# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root is None else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#当去掉self会报错，在class之外的递归函数可以不加self
