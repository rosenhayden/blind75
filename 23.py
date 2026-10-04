#Not optimal but i will improve this later hopefully. O(N*K)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# use our merge two lists function to merge k lists
'''
lists=[l1,l2,l3,lk] such that all l are sorted
merge l1 and l2 to make l12
merge l12 and l3 to make l123
merge l123 and 14 to make l1234
answer = self.mergTwoLists(lists[0],list[1])
for i in range(2, len(lists)):
    self.mergeTwoLists(answer, list[i])

'''
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists :
            return None

        answer = lists[0]
        for i in range(1,len(lists)):
            if lists[i] is not None:
                answer = self.mergeTwoLists(answer, lists[i])
        return answer

    #from problem 21
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        cur = dummy
        # go until both lists are exausted.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        #connect leftovers if they exist
        if list1 is not None:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next
