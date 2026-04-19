# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = mergedList = ListNode()

        while(list1 != None and list2 != None):
            if(list1.val < list2.val):
                mergedList.next = list1
                list1 = list1.next
            else:
                mergedList.next = list2
                list2 = list2.next
            mergedList = mergedList.next

        mergedList.next = list1 if list1 is not None else list2
        return node.next