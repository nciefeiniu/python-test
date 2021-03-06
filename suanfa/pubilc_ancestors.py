# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor(root.left, p, q)
        else:
            return root