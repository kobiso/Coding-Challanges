# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: TreeNode, is_left=False) -> int:

        sum_ = 0
        if root is None:
            return sum_

        if root.left:
            sum_ += self.sumOfLeftLeaves(root.left, is_left=True)
        if root.right:
            sum_ += self.sumOfLeftLeaves(root.right, is_left=False)
        if root.left is None and root.right is None and is_left:
            return root.val

        return sum_
