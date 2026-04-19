# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        curr1 = list1
        curr2 = list2
        new_head = newlist = ListNode(val=0, next=None)

        while(curr1 is not None or curr2 is not None):
            if curr1 is None and curr2 is not None:
                newlist.next = curr2
                break
            elif curr2 is None and curr1 is not None:
                newlist.next = curr1
                break
            else:
                if (curr1.val > curr2.val):
                    newlist.next = curr2
                    curr2 = curr2.next
                else:
                    newlist.next = curr1
                    curr1 = curr1.next 
                newlist = newlist.next
        
        return new_head.next        
