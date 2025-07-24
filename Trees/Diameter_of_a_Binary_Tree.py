# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def findDiameter(root):
            if not root:
                return 0
            nonlocal maxDiameter
            left = findDiameter(root.left)
            right = findDiameter(root.right)
            maxDiameter = max(maxDiameter, left + right)
            return 1 + max(left, right) 
        findDiameter(root)
        return maxDiameter
