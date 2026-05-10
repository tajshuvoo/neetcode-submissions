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

            if curr.left is not None and curr.right is not None:
                temp=curr.left
                curr.left=curr.right
                curr.right=temp

                st.append(curr.left)
                st.append(curr.right)

            elif curr.left is None and curr.right is not None:
                curr.left=curr.right
                curr.right=None

                st.append(curr.right)

            elif curr.left is not None and curr.right is None:
                curr.right=curr.left
                curr.left=None
                
                st.append(curr.left)
            

        return root
        
            
