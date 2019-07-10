# encoding:utf-8
######################第一题##########################
# def maxPoints(points):
# 	size = len(points)
# 	if size  < 3:
# 		return size
# 	ans = 0
# 	for i in range(size):
# 		d = {'inf':0}
# 		samePoint = 1
# 		for j in range(size):
# 			if i == j:
# 				continue
# 			elif points[i][0] == points[j][0] and points[i][1] != points[j][1]:
# 				d['inf'] += 1
# 			elif points[i][0] != points[j][0]:
# 				k = 1.0 * (points[i][1]  - points[j][1] ) / (points[i][0]  - points[j][0] )
# 				if k in d:
# 					d[k] += 1
# 				else:
# 					d[k] = 1
# 			else:
# 				samePoint += 1
# 		ans = max(ans,max(d.values()) + samePoint)
# 	return ans

# p = maxPoints([[0,0],[1,1]])
# print p


########################第二题##########################
# import re

# # 特征
# NUMBER = re.compile(r'[0-9]')
# LOWER_CASE = re.compile(r'[a-z]')
# UPPER_CASE = re.compile(r'[A-Z]')
# OTHERS = re.compile(r'[^0-9A-Za-z]')

#######################第三题##########################

def car(point):
	position=0
	list_position=[]
	
	if point<=2 and point>0:
		list_position.append("A")
		return list_position
	elif point>10000:
		return list_position
	else:
		while position != point:
			if position < point:
				speed =1
				while position < point:
					position += speed
					speed *= 2
					list_position.append("A")
			else:
				speed = -1
				while position > point: 
					position += speed
					speed *= 2
					list_position.append("R")
	list_position.append("A")
	return list_position

a = car(5)
print a
if len(a)==0:
	print "more than maxPoints or mixPoints"
else:
	print len(a)

#######################第5题##########################
# list_envelop=[]
# import itertools
# def sleeve_baby(envelopes):
# 	size = len(envelopes)
# 	enve=0
# 	list_envelop=[]
# 	# j=1
# 	for i in range(size):
# 		for j in range(size-1):
# 			if envelopes[i][0]<envelopes[j][0] and envelopes[i][1]<envelopes[j][1]:
# 				# print envelopes[j][0]
# 				# print envelopes[i][1]
# 				# list_envelop=checkhistory(envelopes[j],list_envelop)
# 				itertools.groupby(envelopes[j])
# 	return list_envelop
# def checkhistory(envelop,envelopes):
# 	if len(envelopes)==0:
# 		return envelopes
# 	for i in range(len(envelopes)):
# 		if envelopes[i][0]<envelop[0] and envelopes[i][1]<envelop[1]:
# 			return envelopes
# 		elif envelopes[i][0]>envelop[0] and envelopes[i][1]>envelop[1]:
# 			return envelopes
# 		# else:
# 		# 	del envelopes[i]
# 		# 	return envelopes
# p = sleeve_baby([[5,4],[6,4],[6,7],[2,3],[1,1],[7,8]])
# print p
# print len(p)






