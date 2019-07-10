# encoding: utf-8
import copy

x =[10]  
a = [x, 20] # a 是个二维数组，x是第一个元素，是list类型，20是第二个元素，int型 
b = a 	# 变量引用，a的值赋给b
c = a[:]  # 求科普，不知道拉～～
d = list(a) # a 强转城list类型，赋值给d
e = a.copy() # 赋值a的值给e，e新开辟内存空间存储a的值
f = copy.copy(a)  # f存储的是a的对象
g = copy.deepcopy(a)  # a的内存地址和值都复制给g

a.append(30)
# x.append(40)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# b, c, d, e, f, g有什么不同  



l1 = [3]
l2 = [5]

def merge(l1,l2):
	result = []

	while l1 and l2:
	    if l1[0] < l2[0]:
	        result.append(l1[0])
	        l1.remove(l1[0])
	    else:
	        result.append(l2[0])
	        l2.remove(l2[0])
	if len(l1)==0:
		result.extend(l2)
	else:
		result.extend(l1)
	# print(result)
	return result

def merge_sort(list1):
	count = len(list1)
	if count<=1:
		return list1
	else:
		l1=list1[:count//2]
		l2=list1[count//2:count]

		result=merge(merge_sort(l1),merge_sort(l2))

		return result

list1=[1,5,3,8,2,9,3,0,4]
# list1 = [9,8,7,6,5,4,3,2,1]
# result=merge_sort(list1)
# print(result)


# 冒泡
# for i in range(len(list1)-1):
# 	for y in range(len(list1)-1-i):
# 		if(list1[y] > list1[y + 1]):
# 			list1[y], list1[y+1] = list1[y+1], list1[y]
# print(list1)


# while len(list1)<=0:
	# max_=list1.max()
# mac = list1.pop(list1(list1.max().index))
# print(mac)

# a = list1(max(list1))
def selectionSort(list1):
	result=[]
	while len(list1)>0:
		a = list1.index(min(list1))
		b = list1.pop(a)
		result.append(b)
	return result

def selectionSort1(list1):
	for y in range(len(list1)-1):
		# print("第%s次"%y)
		for i in range(y+1,len(list1)):
			if list1[i]<list1[y]:
				# print(list1[i],list1[y],"交换")
				list1[y],list1[i]=list1[i],list1[y]
	return list1
# result = selectionSort1(list1)
# print(result)
# result = selectionSort1(list1)

# for y in range(len(list1)-1):
# 	print("第%s次"%y)
# 	for i in range(y+1,len(list1)):
# 		if list1[i]<list1[y]:
# 			print(list1[i],list1[y],"交换")
# 			list1[y],list1[i]=list1[i],list1[y]
# 			print(list1[y])
# 	print(list1)


def inertsort(list1):
	N=len(list1)
	for x in range(1,len(list1)):
		print("x=%s"%x)
		a,b=x,x
		n=list1[x]
		print("n=%s"%n)
		while n<list1[a-1] and a-1>=0:
			a=a-1
			if a-1<0:
				a=0 
		while b>a:
			list1[b]=list1[b-1]
			b=b-1
		list1[a]=n
	return list1
# l=inertsort(list1)
# print(l)



# N=len(list1)
# N=len(list1)

# 从第一个元素开始，该元素可以认为已经被排序；
# 取出下一个元素，在已经排序的元素序列中从后向前扫描；
# 如果该元素（已排序）大于新元素，将该元素移到下一位置；
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
# 将新元素插入到该位置后；
# 重复步骤2~5。

# for x in range(1,len(list1)):
# 	key=list1[x]
# 	a=x
# 	while key<list1[a-1]:
# 		list1[a]=list1[a-1]
# 		a=a-1
# 		if a-1<0:
# 			break
# 	list1[a]=key
# print(list1)

# i=1
# for y in range(len(list1)):

# for i in range(list1):
# 	key= list1[i+1]

# [{"open_id":"oHcCdwhWTXtFFpTaBnHUqTNnL5JQhh","name":"测试10","phone":"13211111120","exts":{"productId":"aaID","FRM":"100","tags":"咖","test":"测试10"}},{"open_id":"oHcCdwhWTXtFFpTaBnHUqTNnL5JQyy","name":"测试11","phone":"13211111121","exts":{"productId":"bbID","FRM":"200","tags":"咖","test":"测试11"}}]:1550229718:abd27528-84c9-4bb4-80a3-4900b30d30f5



# a = "hello"
# b="hello"
# print(a is b)
# print(a==b)

# a="hello world"
# b="hello world"

# print(a is b)
# print(a==b)

a = {
  "actionTime": "2019-01-31 10:57:56",
  "rfm": "111",
  "isHasCoffee": 1,
  "couponRecentExpireTime": "2019-01-31 23:59:59",
  "couponMaximumExpireTime": "2019-02-03 17:52:48",
  "isHasCoffeeBean": 1,
  "cupCount": 1,
  "preferConsumeTime": "不确定",
  "gender": 1,
  "subscribeStatus": 1,
  "registerStatus": 1,
  "singleCategory": "拿铁咖啡",
  "category": "咖啡",
  "channel": "写字楼",
  "type": "商业发展",
  "city": "北京市",
  "pointPositionCode": "BeJ0300042210"
}
keyss=a.keys()
b = sorted(keyss)
print(b)
c=[]
for i in b:
	c.append(str(a[i]))
result = ':'.join(c)
print(result)




