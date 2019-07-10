# encoding:utf-8
# #####################第一题#####################
# import collections

# def feibo(A):
#     size = len(A)
#     if 3 <= size <= 1000:
#         vset = set(A)
#         dp = collections.defaultdict(lambda: collections.defaultdict(int))
        
#         ans = 0
#         for i in range(size):
#             x = A[i]
#             for j in range(i + 1, size):
#                 y = A[j]
#                 if x + y not in vset: continue
#                 dp[y][x + y] = max(dp[y][x + y], dp[x][y] + 1)
#                 ans = max(dp[y][x + y], ans)
#         return ans and ans + 2 or 0
#     else:
#         print("Not long enough!!!")
#         return(0)

# A = [1, 3, 5, 6, 9, 11, 13, 15, 20, 22, 24, 26, 29]
# print(feibo(A))

# A = [111, 123, 234, 256, 335, 444, 465, 543, 631]
# print(feibo(A))
# A = [2740, 8966, 13853, 18315, 29491, 30436, 39147, 39538, 63348, 66510, 74220, 78931, 79588, 82344, 84510, 90275, 92802, 93113, 96210, 98060]
# print(feibo(A))
# A = [77, 116, 211, 248, 285, 285, 422, 438, 491, 496, 526, 532, 568, 742, 795]
# print(feibo(A))
# A = [28, 105, 111, 140, 227, 272, 324, 334, 393, 443, 456, 460, 678, 694, 717, 745, 891]
# print(feibo(A))
# print("#################################################")

# #####################第二题#####################

# def stampSequence(stamp, target):
#     i=0
#     resl=[]
#     if 1 <= len(stamp) <= len(target) <= 1000:
#         while i<10*len(target):
#             if stamp:
#                 pass


#     else:
#         return resl
# # a = stampSequence(stamp = "abca", target = "aabcaca")
# # print(a)
# #####################第三题#####################

# def uniqueMailAddress(mails):
#     mailList=[]
#     for m in mails:
#         b=m.split('@',1)
#         c= b[0].replace('.', '')
#         mailList.append(c[0:c.index('+')]+"@"+b[1])
#     lenght=len(list(set(mailList)))
#     return lenght

# a = uniqueMailAddress(["a.a.a+a@kuick.cn", "a+a+a.a@kuick.cn", "aa.aa+aa@kuick.cn", "aa+a.aa@quick.cn", "aaa+aaa@quick.cn"])
# print(a)
# a = uniqueMailAddress(["a.c.a+a@kuick.cn", "c+a+a.a@kuick.cn", "aa.cc+aa@kuick.cn", "aa.c.c+a.aa@kuick.cn", "ac.a+aaa@k.uick.cn"])
# print(a)
# a = uniqueMailAddress(["abc+cc.a.a@kuick.cn", "a.b.c+a+a.a@kuick.cn", "ab.c+c+aa@kuick.cn", "aa.c.c+a.aa@kuick.cn", "a.ac.c+aaa@kuick.cn"])
# print(a)

# #####################第四题#####################

# def isLongPressedName(name, typed):
#     i, name_len = 0, len(name)
#     for j in range(len(typed)):
#         if i < name_len and typed[j] == name[i]:
#             i += 1
#         elif j == 0 or typed[j] != typed[j-1]:
#             return False
#     return i == name_len

# a = isLongPressedName(name = "java", typed = "jjavvaa")
# print(a)
# a = isLongPressedName(name = "hello", typed = "hheeloo")
# print(a)
# a = isLongPressedName(name = "world", typed = "wwworrllddd")
# print(a)
# a = isLongPressedName(name = "happy", typed = "happpppy")
# print(a)
# a = isLongPressedName(name = "everyday", typed = "eeveevrryddayyy")
# print(a)
#####################第五题#####################

# def fanzhuan(S):
#     size=len(S)
#     mz={}
#     lsn=[]
#     if size <= 100:
#         ls = list(S)
#         for c in range(len(ls)):
#             if 33 <= ord(ls[c])<= 122 and ls[c].isalpha():
#             # if ls[c].isalpha():
#                 lsn.append(ls[c])
#             else:
#                 mz[c] = ls[c]
#         lsn.reverse()
#         mzn=sorted(mz.items(), key=lambda d:d[0])
#         for kv in mzn:     
#             lsn.insert(int(kv[0]), kv[1])
#     else:
#         return "Not long enough!!!"
#     return ''.join(lsn)

def fanzhuan(s):
    l = []
    for i in s:
        if i.isalpha():
            l.append(i)
    temp = []
    for i in s:
        if i.isalpha():
            temp.append(l.pop())
        else:
            temp.append(i)
    result = "".join(temp)
    # l = [i for i in s if i.isalpha()]
    # result = "".join([i if not i.isalpha() else l.pop() for i in s])
    return result
        



# ll = fanzhuan("a-B+c*d-e!F&e")
# print(ll)
# ll = fanzhuan("R+bC=d(Ef)-g^h#I!j==I")
# print(ll)
# ll = fanzhuan("K--U=i%%c@KD~ea,L")
# print(ll)
# ll = fanzhuan("h$E))ll__O,W**or#!LD")
# print(ll)
#####################第六题########################



def func(s):
    l = list(s) #模拟全部入栈
    result = ""
    while len(l)>0:
        result += l.pop() #模拟出栈,pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    return result

if __name__ == '__main__':
    r = fanzhuan("ku!a！it--u+i")
    print(r)






