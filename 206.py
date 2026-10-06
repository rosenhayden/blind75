
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        cur = head
        temp = None
        last=None
        while cur != None:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
        return last
