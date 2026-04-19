# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None or head.next is None):
            return False
        curr = head

        while(curr.next is not None):
            
            print(curr.val)
            if curr.val is None:
                return True
            curr.val = None
            curr = curr.next
        return False