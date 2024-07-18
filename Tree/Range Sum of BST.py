# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rec(root):
            if not root:
                return 0
            elif root.val<low:
                return rec(root.right)
            elif root.val>high:
                return rec(root.left)
            return root.val+rec(root.right)+rec(root.left)
        return rec(root)
