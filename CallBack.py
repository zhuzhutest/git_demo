# coding=utf-8
import requests
import json
import sys
import datetime 
reload(sys)  
sys.setdefaultencoding('utf8')   
def clean1(times):
    """
    就假装是扫地吧，这种函数命名方式，千万别学习
    :param times: 次数
    :return: None
    """
    print '已完成扫地次数:', str(times)
 
def clean2(times):
    """
    默默的装作洗抽油烟机
    :param times: 次数
    :return: None
    """
    print '已洗抽油烟机次数', str(times)
 
 
def call_clean(times, function_name):
    """
    这个很重要，这个就是家政公司的业务系统，要啥业务都得在这说
    这个是实现回调函数的核心
    :param times:次数
    :param function_name:回调函数名
    :return:调用的函数结果
    """
    return function_name(times)

def call_auth(token):
    token="bbbbbbbbbbbbbbbbbbbbbbbbb"
    return token
    

def get_url(token,function_name):
    res = requests.get("https://deal-api-test2.kuick.cn/api/v1.0/user/123199/received-hyper-cards?access_token=1b029fe2afd437c63bcf29a4d41a11a4532ed584364ceed65af4bcd50e3e1be3de802f95c715846f08de0ff9eeb1ebb9228db700827356acda22fa6bdf639960")
    res.status_code=401
    print res.status_code
    if res.status_code==401:
        return function_name(token)

def getSwarmLIst(longin):
    count=1
    index=1
    for index in range(longin):
        if count < 20:
            starttime = datetime.datetime.now()
            url="https://deal-admin-test3.kuick.cn/api/v1.7/app/301ac74e-4dc4-4923-8461-b5b77532261f/customer-swarm/ab9f6a58-19e4-45a0-9c50-e1adf0514f5e/members?access_token=f59bed89502cadf58d60896d1bac58678cfe3662202665b1fa988fdfe7b0dae00273469e2087886b0fd9c8447f7258bb7189d247a60d4e0d3486a796dbb29895&app_secret=bb1549b9-4981-4b38-a9a8-d4b95cb69427&https=1&kuick_user_id=494&customer_owner_id=494&group_id=all&keyword=&start_index=%s"%index
            res=requests.get(url)
            body= json.loads(res.text)
            swcl=body['data']
            print len(swcl)
            endtime = datetime.datetime.now()
            mirs=(endtime-starttime).microseconds
            print mirs/1000
            count += 1
            index += 20
        else:
            count=1
if __name__ == '__main__':
    getSwarmLIst(10000)
    # call_clean(100, clean2) # 给我洗100次抽油烟机，好吧，很变态
    # token=get_url("abcabc",call_auth)
    # print token

    # /Users/zhu/workspace_for_api/script/CallBack.py
