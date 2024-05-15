# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # create a dummy node
        p = dummy = ListNode(-1)
        # use heapq to store head nodes
        hq = []
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(hq, (lists[i].val, i, lists[i]))
        
        while hq:
            # pop the minimum node, add it to new list
            temp = heapq.heappop(hq)[2]
            p.next = temp
            # add next node to heapq
            if temp.next:
                i += 1
                heapq.heappush(hq, (temp.next.val, i, temp.next))
            # move pointer forward
            p = p.next
        
        return dummy.next
