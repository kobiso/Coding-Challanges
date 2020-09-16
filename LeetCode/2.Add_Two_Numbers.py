"""
Author: Byungsoo Ko
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_res = None
        carry = False
        while l1 or l2:
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            cur_sum = first_val + second_val
            if carry:
                cur_sum += 1
            if cur_sum >= 10:
                carry = True
                cur_sum = cur_sum-10
            else:
                carry = False

            cur_res = ListNode(cur_sum)
            if pre_res is None:
                result = cur_res
            else:
                pre_res.next = cur_res
            pre_res = cur_res
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            cur_res = ListNode(1)
            pre_res.next = cur_res
        cur_res.next = None

        return result
