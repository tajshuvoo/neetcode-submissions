# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp is not None:
            temp=temp.next
            count+=1

        new_count=0
        temp=head
        if count-n==0:
            return head.next
            
        while temp is not None:
            prev=temp
            temp=temp.next
            new_count+=1

            if new_count==(count-n):
                prev.next=temp.next
                break

        return head
        