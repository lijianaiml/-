# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        len_row = len(array)
        len_col = len(array[0])
        row = len_row - 1
        col = 0
        while(row >= 0 and col <= len_col - 1):
            if target > array[row][col]:
                col += 1
            elif target < array[row][col]:
                row -= 1
            else:
                return True
        return False
