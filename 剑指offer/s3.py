# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 1. 递归实现
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is not None:
            return self.printListFromTailToHead(listNode.next) + [listNode.val]
        return []
        
        # 2. 堆栈实现
        
        # 3. 列表反序实现
    def printListFromTailToHead2(self, listNode):
        list_rev = []
        while listNode is not None:
            list_rev.append(listNode.val)
            listNode = listNode.next
        return list_rev[::-1]