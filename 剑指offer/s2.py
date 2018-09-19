# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
    
    def replaceSpace2(self, s):
        res=[]
        liststr=list(s)
        for s in liststr:
            if s == ' ':
                res.append('%20')
            else :
                res.append(s)
        return ''.join(res)
    
    if __name__ == '__main__':
        replaceSpace2()
