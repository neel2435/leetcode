# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = list1
        second = list2
        merged = ListNode(0)
        dummy = merged

        while first and second:
            if first.val <= second.val:
                merged.next = first
                first = first.next
            else:
                merged.next = second
                second = second.next
            merged = merged.next

        if first == None:
            merged.next = second
        elif second == None:
            merged.next = first

        return dummy.next