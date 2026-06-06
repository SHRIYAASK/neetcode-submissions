# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            temp1=list1
            temp2=list2
            curr=ListNode(0)
            dummy=curr
            while temp1 is not None and temp2 is not None:
                if temp1.val<=temp2.val:
                    dummy.next=temp1
                    temp1=temp1.next
                else:
                    dummy.next=temp2
                    temp2=temp2.next
                dummy=dummy.next
            if temp1 is not None:
                dummy.next=temp1
            else:
                dummy.next=temp2
        return curr.next





        