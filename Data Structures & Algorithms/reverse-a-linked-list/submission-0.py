# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[] 
        temp=head
        while temp:
            a.append(temp.val)
            temp=temp.next
        a.reverse()
        temp=head
        for i in range(0,len(a)):
            temp.val=a[i]
            temp=temp.next
        return head
    

            
        