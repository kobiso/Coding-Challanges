# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Runtime: 28 ms, faster than 99.88% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.2 MB, less than 43.66% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        idx_to_node = {}
        idx = 0
        
        cur_head = head
        while cur_head:
            idx_to_node[idx] = cur_head
            cur_head = cur_head.next
            idx += 1
        find_idx = idx - n
        if idx == 0:
            return None
        if find_idx-1 < 0:
            if idx_to_node[find_idx].next:
                head = idx_to_node[find_idx].next
            else:
                head = None
        else:
            if idx_to_node[find_idx].next:
                idx_to_node[find_idx-1].next = idx_to_node[find_idx].next
            else:
                idx_to_node[find_idx-1].next = None
        return head