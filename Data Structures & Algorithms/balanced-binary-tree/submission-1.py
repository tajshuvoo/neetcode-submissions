# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced=True
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Definition for a binary tree node.
        if root is None:
            return True
        st=[root]
        while len(st)>0:
            root=st.pop()

            left= self.maxDepth(root.left)
            right= self.maxDepth(root.right)

            if abs(left-right)>1:
                self.balanced=False

            if root.left:
                st.append(root.left)
            if root.right:
                st.append(root.right)
        
        return self.balanced