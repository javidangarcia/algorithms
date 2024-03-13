# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = self.reverse(slow.next)
        slow.next = None

        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Time: O(n)
# Space: O(1)