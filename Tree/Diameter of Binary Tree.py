# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root,diameter):
            if not root:
                return 0
            ldepth=depth(root.left,diameter)
            rdepth=depth(root.right,diameter)
            diameter[0]=max(diameter[0],ldepth+rdepth)
            return max(ldepth,rdepth)+1
        diameter=[0]
        depth(root,diameter)
        return diameter[0]        
