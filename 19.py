# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = head
        count = 0
        while dummy:
            dummy = dummy.next
            count += 1
        if count <= 1:
            return None
        target = count - n
        i=0
        last = None
        newHead = head
        while i != target:
            last = head
            head = head.next
            i+=1
        if last:
            last.next = head.next
            head = None
        else:
            newHead = head.next #edge case of when n is the first element, simply skip over it
        return newHead
