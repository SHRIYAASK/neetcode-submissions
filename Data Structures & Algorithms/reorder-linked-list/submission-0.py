class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        i, j = 0, len(arr) - 1
        dummy = ListNode(0)
        curr = dummy

        while i <= j:
            curr.next = arr[i]
            curr = curr.next
            i += 1

            if i <= j:
                curr.next = arr[j]
                curr = curr.next
                j -= 1

        curr.next = None