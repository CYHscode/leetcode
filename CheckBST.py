# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isvalid(self, root, small, large):
        if root is None:
            return True
        if root.val >= large or root.val <= small:
            return False
        return self.isvalid(root.left, small, root.val) and self.isvalid(root.right, root.val, large)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isvalid(root, -2**32, 2**32-1)
        
#在思考过程中考虑像计算深度一样的递归实现该题， 但在编写过程中发现不合适，比如出现两个错误问题时返回了true。。。。。。
#在参考答案时发现根据二叉搜索树的性质最大最小的位置并记录值是一个好方法，如上所示
