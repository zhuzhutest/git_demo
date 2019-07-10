# encoding: utf-8
# coding=codeing:gb18030
##############第一题###############
def firstChar(s):
    s_list = list(set(s))
    s_list.sort(key= s.index)
    for value in s_list:
        if s.count(value) == 1 and value.isalpha():
            return s.index(value)
    return -1

print("=======第一题=======")
s = "helloworld"
print(firstChar(s))
s = "beebeef"
print(firstChar(s))
s = "alpha"
print(firstChar(s))
s = "helloworldhelloworld"
print(firstChar(s))
s = ""
print(firstChar(s))
###############第二题#################
def mergeSection(section):
    if len(section) ==1:
        return section
    elif len(section)<1:
        return 0
    else:
        secStrat = []
        for i in range(len(section)-1):
            if section[i][1]>=section[i+1][0]:
                secStrat.append([section[i][0],section[i+1][1]])
                i=i+2
            else:
                secStrat.append([section[i][0],section[i][1]])
        return secStrat
print("=======第二题=======")
li = [[1,3],[8,10],[2,9],[12,15],[3,4],[15,22]]
print(mergeSection(li))
li = [[3,5],[2,4],[8,11],[13,14],[14,16]]
print(mergeSection(li))
##################################

###############第三题#################
def water(x, y, z):
    if z == 0:
        return True
    if x+y < z:
        return False
    if x>y:
        x,y=y,x
    if x == 0:
        return y==z
    while y%x != 0:
        y,x = x,y%x
    return z%x==0
print("=======第三题=======")
x=3
y=5
z=10
print(water(x , y, z ))
x = 2
y = 6
z = 11
print(water(x , y, z ))
##################################

###############第四题###################
print("=======第四题=======")
print("不会不会………………谷大坑！！！")
##################################

###############第五题###################
# def operation(num,target):
#     a = list(num)
#     if len(a)<1:
#         return -1
#     elif len(a)==1:
#         if int(a[0])==target:
#             return ("不成立")
#     else:
#         i=0
#         while i<=len(a):
#             j = target-int(a[-1])
#             ja = target+int(a[-1])
#             c = int(target / int(a[-1]))
#             print(j,ja,c)



# num = "123",target = 6
print("=======第五题=======")
print("不会不会………………谷大坑！！！")
# operation(num = "123",target = 6)
###############第6题###################

import math
def pigs(n, m, p):
    return int(math.ceil(math.log(n,p/m)))
print("=======第六题=======")
n = 25
m = 15 
p = 60
print(pigs(n,m,p))
n = 1000
m = 15
p = 60
print(pigs(n,m,p))



