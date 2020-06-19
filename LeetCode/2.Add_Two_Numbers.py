# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(m+n+max(m,n))
    # Runtime: 88 ms, faster than 90.13% of Python3 online submissions for Add Two Numbers.
    # Memory Usage: 13.3 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
    def listToDigit(self, linked_list):
        
        digit_str=''
        while (not isinstance(linked_list, type(None))):
            digit_str = str(linked_list.val) + digit_str
            linked_list = linked_list.next            
        
        return int(digit_str)

    # O(max(m,n))
    # Runtime: 108 ms, faster than 56.86% of Python3 online submissions for Add Two Numbers.
    # Memory Usage: 13.3 MB, less than 5.21% of Python3 online submissions for Add Two Numbers.
    def sumCarry(self, l1, l2):
        result = []
        carry = False        
        while ((not isinstance(l1, type(None))) or (not isinstance(l2, type(None))) or carry):
            
            if isinstance(l1, type(None)): l1_val = 0
            else: l1_val = l1.val
            if isinstance(l2, type(None)): l2_val = 0
            else: l2_val = l2.val

            if carry: sum_val = l1_val + l2_val + 1
            else: sum_val = l1_val + l2_val
                
            if sum_val >= 10:
                carry = True
                sum_val = sum_val-10
            else: carry = False

            result.append(sum_val)
            if not isinstance(l1, type(None)): l1 = l1.next
            if not isinstance(l2, type(None)): l2 = l2.next
        return result
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # return list(map(int, str(self.listToDigit(l1) + self.listToDigit(l2))[::-1]))
        return self.sumCarry(l1,l2)