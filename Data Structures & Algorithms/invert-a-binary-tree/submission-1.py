# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        

        st=[]
        st.append(root)
        
        while len(st)>0: 
            curr=st.pop()
        
            temp=curr.left
            curr.left=curr.right
            curr.right=temp

            if curr.left is not None:
                st.append(curr.left)
            if curr.right is not None:
                st.append(curr.right)

        return root
        
            
