# encoding:utf-8
######第一题#########
class Jiao():	
	def fun(self,n):
		nlist=[]
		while n!=1:
			if n%2==0:
				n = n/2
				nlist.append(n)
			else:
				n = n*3+1
				nlist.append(n)
		print "No number can be output !"
		return nlist

b=Jiao()
jiao = b.fun(3)
print jiao
######第二题#########
# 有n个人站成一列。并从头到尾给他们编号，第一个人编号为1。
# 然后从头开始报数，第一轮依次报1，2，1，2...然后报到2的人出局。
# 接着第二轮再从上一轮最后一个报数的人开始依次报1，2，3，1，2，3...报到2，3的人出局。
# 以此类推直到剩下以后一个人。现在需要求的即是这个人的编号。

# 给定一个int n，代表游戏的人数。请返回最后一个人的编号

class Joseph:
	def result(self, n):
		count=[i for i in range(1,n+1)]
		res=n
		round=2
		while res>1:
			for i in range(len(count)):
				if (i+1)%round!=1:
					count[i]=-1
					res-=1
			count=[i for i in count if i!=-1]
			count.insert(0,count.pop())
			round+=1
		return count[0]

# a = Joseph()
# b= a.result(23)
# print b

#################第三题#########
class Robot:
	def countWays(self, m,x, y):
		# write code here
		if x<=0 or y<=0:
			return 0
		res = []
		for i in range(x):
			tmp = []
			for j in range(y):
				tmp.append(0)
			res.append(tmp)
		res[0][0] = 1
		for i in range(1,x):
			res[i][0] = res[i-1][0]
		for i in range(1,y):
			res[0][i] = res[0][i-1]
		for i in range(1,x):
			for j in range(1,y):
				res[i][j] = res[i-1][j]+res[i][j-1]
		return res[x-1][y-1]
# robot = Robot()
# r = robot.countWays([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,1],[0,1,1,1],[1,1,1,1],[1,1,1,1]],11,4)
# print r



############第四题###########
i=1
n=10
m=10
for i in range(n-2):
	j=i+1
	for j in range(n-1):
		k=j+1
		for k in range(n):
			last=0
			cnt=0
		t=1
		for t in range(m-1):
			pass

