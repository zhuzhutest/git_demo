#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import threading
from time import ctime,sleep

uri='http://deal.kuick.cn/link/d0dab477-bc0b-40f2-85be-7d3102114920?share_token=ESJjWGH3'



def xingwei(i):
    print i
    uri = 'http://deal-test3.kuick.cn/api/v1.0/link/b505d83c-8f9f-4c8e-b8fb-3a243138cf42/view-logs?share_token=qGXF8OAW'


    headers= {
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie":"user=b087e67a28ae1878253ff0a290b4d4f925cef8e45fc0f1bbfcada673315cbf78dd26f39aa7b95ab186fcb70b2b65dc92749af20e397e12b6c0d565ba06080add7eb833e07ad80a8398107a530567944addfcc5e17e7f942bcdc20950687ba35b7543d47e8d6f17e95c109ec1cc26101fe9d095a7f5930183eca4b02ced3382c6f28e14aed525a0b51e866d89a213eb39fe3b8fd0de57e4ecc6084f4b08853f6e6f66c41a9907e4f0fcdd72f591574ea00407a0a2be26fc78f16c355f8d87bd1b; guest_id=1d9db698-f96b-4f84-b452-1ed53695aef3; user_name=Guest-95aef3; user_photo_url=https%3A%2F%2Fimg-prod.kuick.cn%2Fuser%2Fheader%2Fguest.png; gr_user_id=f1849bba-7694-4b7e-a85d-13ffbbd48478; kd_user_id=1ed6eb4f-75fe-473f-b493-2641ed835c12; gr_session_id_59cccc317187497c97ee089aff248594=3346970f-806e-434e-bca9-bc991aa9937b; connect.sid=s%3A0d6d952c-5765-4ab3-b329-598b70594d8b.oxeJewpyi8Xg13zL28veKGaWODJQpOiwZyTpYi%2Byy7o; CONTAINERID=e0358a7df6d9e27595769c7197128a48cce1039ff908c532083a1cede7d40067",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    body = {
        "viewer_id":"bb4a9db3-7b0a-4b57-8c31-f283cc4bbc1e",
        "viewer_name":"",
        "system":"OS+X+10.12",
        "client":"Firefox+56.0"
    }
    res = requests.post(uri,body,headers)
    print res
def jinyan(i):
    print i
    uri = "http://deal-test3.kuick.cn/api/v1.0/link/d5faf86a-48fd-41ee-a173-5a6c1883de47/view-logs?share_token=qGXF8OAW"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"user=d43c09b06c0cea1b91c63e2bd244e43d917fadad77fd9e225521b2c0791fec31566c26537c6ab7a189f2356ed6eab5f6749af20e397e12b6c0d565ba06080addb4193b2769b4e3e57fa38e38269cd737ddfcc5e17e7f942bcdc20950687ba35b7543d47e8d6f17e95c109ec1cc26101fe9d095a7f5930183eca4b02ced3382c6f28e14aed525a0b51e866d89a213eb39fe3b8fd0de57e4ecc6084f4b08853f6e6f66c41a9907e4f0fcdd72f591574ea00407a0a2be26fc78f16c355f8d87bd1b; guest_id=ea415a84-be35-461c-9ef4-162aebed864b; user_name=Guest-ed864b; user_photo_url=https%3A%2F%2Fimg-prod.kuick.cn%2Fuser%2Fheader%2Fguest.png; kd_user_id=30355968-7a9a-4e19-acb6-a7d4979c9775; gr_user_id=a69e75f6-a84c-440a-ae6d-eab6b52ca614; gr_session_id_59cccc317187497c97ee089aff248594=7779734c-f768-4e7d-8362-d25d0e0a9073; connect.sid=s%3Ad86dc76c-1368-46ef-8816-1a24e9e5c51c.7Fv%2BigEnk6NCnGF1K49NrsWC9i002Tt%2FIRrI09M%2BYpY; CONTAINERID=8983fb467854c869b013586228e5c44f00ce00bfb5a7e31e96a162192e5a2409",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",  
    }
    body = {
        "viewer_id":"7c54511e-dee4-4052-9982-d8814c85b06b",
        "viewer_name":"",
        "system":"Windows NT 10.0 64-bit",
        "client":"Chrome 60.0.3112.78"
    }
    res = requests.post(uri,body,headers)
    print res

threads = []
for i in range(50):
    t1 = threading.Thread(target=xingwei,args=(i,))
    threads.append(t1)
    t2 = threading.Thread(target=jinyan,args=(i,))
    threads.append(t2)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        sleep(0.5)
        t.setDaemon(True)
        t.start()

    print "all over %s" %ctime()

# body = {
#   "name": "zhuzhutest37",
#   "title": "",
#   "email": "",
#   "phone": "15210865179",
#   "company": "",
#   "sex": 2,
#   "province": "",
#   "city": "",
#   "county": "",
#   "address": "",
#   "age_state": -1,
#   "fixed_phone": "",
#   "kuickUserId": "",
#   "lead_source": "",
#   "grade": "",
#   "industry": "",
#   "intentionality": "",
#   "from": "",
#   "get_way": "",
#   "promoter_id": "",
#   "from_content_title": "",
#   "from_content_link": "",
#   "search_keyword": "",
#   "buyed_keyword": "",
#   "platform": "",
#   "create_way": 6,
#   "from_province": "",
#   "from_city": "",
#   "utm_medium": "",
#   "utm_campaign": "",
#   "utm_content": "",
#   "source": "singleCreate",
#   "deal_user_id": null
# }