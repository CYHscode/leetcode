# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        1.cur = head
        head1 = ListNode(0)
        while cur is not None:
            temp = ListNode(cur.val)
            temp.next = head1.next
            head1.next = temp
            cur = cur.next
        return head1.next
        
        2.head1 = None
        while head is not None:
            cur = head
            head = head.next
            cur.next = head1
            head1 = cur
        return head1
        
#1,2区别在于是否新建节点，结果1会消耗空间和时间
