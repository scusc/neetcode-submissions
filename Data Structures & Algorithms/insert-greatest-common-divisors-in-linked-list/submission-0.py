# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getGcd(self, n1, n2):
        a = n1
        b = n2
        while True:
            if a == 0:
                return b
            if b == 0:
                return a
            a, b = b, a%b

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            n1, n2 = cur.val, cur.next.val
            cur.next = ListNode(self.getGcd(n1, n2), cur.next)
            cur = cur.next.next
        return head