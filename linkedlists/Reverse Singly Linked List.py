class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, temp, prev = head, None, None

        while curr:
            temp = curr.next # save the next
            curr.next = prev # point the first node to None (1 -> None)
            prev = curr # save current node
            curr = temp # iterate the current node

        # for [1, 2, 3, 4]
        
        # temp = 2
        # 1 points to None
        # curr node becomes 2

        # temp = 3
        # 2 points to 1 points to None
        # curr node becomes 3

        # temp = 4
        # 3 points to 2 points to 1 points to None
        # curr node becomes 4

        # temp = None (end of list)
        # 4 points to 3 points to 2 points to 1 points to None
        # curr node becomes None and breaks the loop

        return prev

