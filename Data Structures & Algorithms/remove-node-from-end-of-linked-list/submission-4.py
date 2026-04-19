class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (like removing the head itself)
        dummy = ListNode(0, head)
        
        # Initialize both pointers at the dummy node
        slow = dummy
        fast = dummy
        
        # 1. Give 'fast' a head start of n + 1 steps 
        # (n+1 so that slow lands *right before* the node to delete)
        for _ in range(n + 1):
            fast = fast.next
            
        # 2. Move both pointers at the same speed until fast hits the end
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # 3. 'slow' is now exactly before the node we want to remove.
        # Bypass the target node.
        slow.next = slow.next.next
        
        # Return the actual head of the list (dummy.next handles if head was deleted)
        return dummy.next