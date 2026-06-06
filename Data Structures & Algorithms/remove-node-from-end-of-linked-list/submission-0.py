# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.pop(-n)
        if not arr:
            return None
        temp=head
        x=len(arr)
        for i in range(x):
            temp.val=arr[i]
            prev=temp
            temp=temp.next
        prev.next=None
        return head 

