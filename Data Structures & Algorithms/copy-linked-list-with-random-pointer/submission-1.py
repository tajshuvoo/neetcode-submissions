"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return []

        hash_t={}
        node=Node(head.val)
        hash_t[head]=node
        temp=node
        h=head
        h=h.next
        

        while h is not None:
            temp.next=Node(h.val)
            temp=temp.next
            hash_t[h]=temp
            h=h.next

        t2=node
        while head is not None:
            t2.random= None if head.random==None else hash_t[head.random]
            t2=t2.next
            head=head.next
        return node