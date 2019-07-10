# import unittest

# def binDecimal(num):
#     i=0
#     strnum=""
#     # a = equ(num,0)
#     while not equ(num,0):
#         i+=1
#         if i>32:
#             break
#             return "Error" 
#         num=num*2
#         # print num
#         if equ(num, 1):
#             strnum+="1"
#             num-=1
#             # print "1:"
#             # print strnum
#         else:
#             strnum+="0"
#             strnum="".join("0")
#     return "0."+strnum

# def equ(num,n):
#     b = num-n
#     print b
#     print "=====-===++++"
#     if num  - n< 1.0000001 and num -n > -0.000000001:
#         return True
#     else:
#         return False

# if __name__ == '__main__':
#     a = binDecimal(0.625)
#     print a
    # if(num< 0.0000001 && num -n > -0.000000001)
    #     return true;
    #     else return false;







# class testABC(unittest.TestCase):
#     """docstring for testABC"""
#     @classmethod
#     def setUpClass(self):
#         print "abc"
#     def tearDownClass(self):
#         print "def"
#     def testABCc():
#         return Success

# if __name__ == '__main__':
#     unittest.main()


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2==[]:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()


# import java.util.*;
 
# public class BinDecimal {
#     public String printBin(double num) {
#         // write code here
#         StringBuilder sb = new StringBuilder();
#         int i = 0;
#         while(!equal(num,0)){
#             i ++;
#             if(i > 32) break;
#             num = num * 2;
#             if(equal(num, 1)) {
#                 sb.append(1);
#                 num = num  -1;
#             }  
#             else
#                 sb.append(0);
               
#         }
#         if(i > 32) return "Error";
#         else return "0." +sb.toString();
        
#     }
#     public boolean equal(double num,int n){
#         if(num  - n< 0.0000001 && num -n > -0.000000001)
#             return true;
#         else return false;
#     }
# }






