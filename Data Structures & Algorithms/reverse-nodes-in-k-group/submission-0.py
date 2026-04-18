# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0

        while group < k and cur:
            cur = cur.next
            group += 1
        
        if group == k:
            cur = self.reverseKGroup(cur, k)
            while group > 0:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                group -= 1
            
            head = cur
        return head
        