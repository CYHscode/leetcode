# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:       
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.cmpLR(root.left, root.right)
        
    def cmpLR(self, left, right):
        if not left and not right:
            return True
        elif left and right and left.val == right.val:
            return self.cmpLR(left.left, right.right) and self.cmpLR(left.right, right.left)
        else:
            return False

#二叉树递归解决问题关键是return值的选择，在这一题关键是self.cmpLR(left.left, right.right) and self.cmpLR(left.right, right.left)
#对比昨天的计算二叉搜索树的问题，同是计算return的条件，可以从一般提取出条件
