# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        i=0
        while l1 is not None:
            n1+=(l1.val*(10**i))
            i+=1
            l1=l1.next

        n2=0
        j=0
        while l2 is not None:
            n2+=(l2.val*(10**j))
            j+=1
            l2=l2.next

        sum=n1+n2

        head=ListNode(sum%10)
        sum=sum//10
        t=head
        while sum:
            
            t.next=ListNode(sum%10)
            sum=sum//10
            t=t.next

        t.next=None

        return head