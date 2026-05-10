# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        st1=[p]
        st2=[q]

        while len(st1)>0:
            p=st1.pop()
            q=st2.pop()

            if p.val==q.val :
                if p.left  and q.left :
                    st1.append(p.left)
                    st2.append(q.left)
                elif p.left is None and q.left is not None:
                    return False
                elif p.left is not None and q.left is None:
                    return False

                if p.right and q.right :
                    st1.append(p.right)
                    st2.append(q.right)
                elif p.right is None and q.right is not None:
                    return False
                elif p.right is not None and q.right is None:
                    return False

            else:
                return False

        return True

                