# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        current = head

        while current and current.next:
            if current.val <= current.next.val:
                current = current.next
            else:
                extracted = current.next
                current.next = current.next.next

                prev = dummy
                while prev.next and prev.next.val <= extracted.val:
                    prev = prev.next

                extracted.next = prev.next
                prev.next = extracted      

        return dummy.next
