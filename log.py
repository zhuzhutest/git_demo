import re
import json
from collections import defaultdict


#     # count = defaultdict(int)
#     # print count
    
# def play_click():
# 	pass


import random
# def bubble_sort(data):
# 	length = len(data)
# 	for i in range(len(data) - 1):
# 		for j in range(len(data) - 1):
# 			if (data[j] < data[j + 1]):
# 				tmp = data[j]
# 				data[j] = data[j + 1]
# 				data[j + 1] = tmp
# def bubble_sort(data):
# 	length = len(data)
# 	for i in range(length):
# 		for j in range(length):
# 			if data[j] == data[j+1]:
# 				# print data[j]
# 				index = data.index(data[j])
# 				print index
# 				break
# 		break
# # data = ['a', 'b', 'c', 'c', 'd', 'e', 'f']

# def split_string(data):
# 	b = []
# 	print data
# 	for i in range(len(data)):
# 		b.append(data[i])
# 	return b
# # print data, len(data)
# b = split_string("abccddeeffg")
# bubble_sort(b)
# print data

# FEED
# EDITION
# PLAYDETAIL
# NOTIFICATIONINAPP
# AD
# ALERTVIDEO


# ios
# YOUTUBE_WEB_IFRAME
# YOUTUBE_WEB  server
# FACEBOOK_H5
# FACEBOOK_WEB  server

# android
# YOUTUBE_SDK
# 
# YOUTUBE_WEB
# FACEBOOK_NATIVE
# FACEBOOK_WEB





def split_string(data):
	chars = []
	for i in range(len(data)):
		chars.append(data[i])
	return chars

def bubble_sort(data):
	length = len(data)
	# index = 0
	for i in range(0,length):
		print i
		print "+++++++++"
		for x in range(i+1,length):	
			if data[i] == data[x]:
				print "index is "+str(i)
				break
			else:
				print "don't same"
	return
string = "abcdeffg"
bubble_sort(string)

