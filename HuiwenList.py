# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        a = []
        while cur:
            a.append(cur.val)
            cur = cur.next
        l = len(a)
        for i in range(int(l/2)):
            if a[i] != a[l-i-1]:
                return False
        return True
        
#range()内不能是float 如len(a)/2，这样转成int()或整除符号//
