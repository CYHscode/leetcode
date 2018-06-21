# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:   
            return None
        curr = head
        node = []
        while curr is not None:
            node.append(curr)
            curr = curr.next
        if n == 0:
            node[-1].next = None
        elif n == len(node):
            head = node[1]
        else:
            node[len(node)-n-1].next = node[len(node)-n].next
        return head
       
 #链表结构中判断是否为空最好用is None
 #is 和 ==的区别：is 是指相同的对象 ==是指值相等
