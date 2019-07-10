#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from time import sleep, ctime 
import requests
from multiprocessing import Process
import time
import threading
import random
import logging
import mysql
import mysql.connector as sql
import os
import json
import uuid
 
exitFlag = 0
 
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print thredNum
        fo = open("/Users/zhu/Downloads/test1.log", "r")
        for i in range(thredNum):
            line = fo.readline()
            logging.info("========= %s =========" %line)
            # inseartDB()
            # if i%thredNum==0:
            customerId=create_customer(i)
            print "========= customerId: %s ========="%customerId
            dealUserId=create_dealuser(line)
            print "========= dealUserId: %s ========="% dealUserId
            cldu=customer_link_deal_user(customerId,dealUserId)
            fans(customerId,dealUserId,line)
        fo.close()

        # print "Starting " + self.name
        # abc(self.name, self.q)
        # print "Exiting " + self.name
 
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data) 
        else:
            queueLock.release()
        # time.sleep(1)

def abc(threadName,q):
    print "fangfa"
    print threadName
    print q
threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4","Thread-5","Thread-6","Thread-7"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1
 
# 创建新线程
for tName in range(10):
    thread = myThread(threadID, "Thread-zhu"+str(tName), workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
 
# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
 
# 等待队列清空
while not workQueue.empty():
    pass
 
# 通知线程是时候退出
exitFlag = 1
 
# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"