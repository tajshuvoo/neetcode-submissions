# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans=[]
        st=[]

        st.append(root)
        curr=root.left

        while curr is not None or len(st)>0:
            
            while curr is not None:

                st.append(curr)
                curr=curr.left

            res=st.pop()
            ans.append(res.val)

            curr= res.right

        return ans