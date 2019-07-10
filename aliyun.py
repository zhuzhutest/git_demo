# encoding: utf-8
import requests
import json
import threading
import sys
import csv
from time import ctime,sleep
reload(sys)

sys.setdefaultencoding('utf8')

import csv
with open('/Users/zhu/workspace_for_api/script/TestData6.csv', 'rb') as f:	# 采用b的方式处理可以省去很多问题
	reader = csv.reader(f)
	for row in reader:
		print row


# def search(i):
# 	try:
# 		uri = "https://deal-admin-test3.kuick.cn/api/v1.6/app/2717e413-9ed2-4115-9e16-099e607164e4/member/494/customer/search?condition=zhuguoliang@kuick.cn&has_phone=0&access_token=5f206414f30951771c89beabd8d7ac047a7606e698ae05dc1d9483d4ffd8262d9e192348c2be98aea4ba2ac80d4e9ae062071f607cb44b39a8a1b3c9d3cc931d&app_secret=da9ee5a6-3cb4-4887-b421-0599579bf922&_method=GET&callback=__jp5"
# 		print "I was listening to %s. %s" %(i,ctime())
# 		res = requests.get(uri)
# 		print res.status_code
# 	except Exception, e:
# 		raise e
	
# threads = []
# for i in range(500):
# 	t1 = threading.Thread(target=search,args=(i,))
# 	threads.append(t1)

# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#         sleep(0.2)
#     t.join()
#     print "all over %s" %ctime()

# uri = "https://msp.aliyun.com/HomeAjax/GenerateIsvUrl.json"

# header={":authority":"msp.aliyun.com",
# ":method":"POST",
# ":path":"/HomeAjax/GenerateIsvUrl.json",
# ":scheme":"https",
# "accept":"*/*",
# "accept-encoding":"gzip, deflate, br",
# "accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
# "content-length":"363",
# "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
# "cookie":"cnz=rf51EsKtyUoCAYI8DNIvFsfx; login_aliyunid='44848****@qq.com'; login_aliyunid_ticket=GHnsb86zWRbZQE_oQxtgRUE1_Iupof_BNTwUhTOoNC1ZBeeMfKJzxdnb95hYssNIZor6q7SCxRtgmGCbifG2Cd4ZWazmBdHI6sgXZqg4XFWQfyKpeu*0vCmV8s*MT5tJl3_1$$wId52baweND54y0B110; login_aliyunid_csrf=_csrf_tk_1465508839620858; login_aliyunid_pk=1977027351032533; hssid=1_DY1eecgO4mAcFehv-0fhA1; hsite=6; aliyun_country=CN; aliyun_site=CN; aliyun_lang=zh; JSESSIONID=R1666Y61-2XDPPGDQPIK2PPSFCRMX1-XOW9G59J-2O1; tmp0=eNrz4A12DQ729PeL9%2FV3cfUxiKzOTLFSCjI0MzOLNDPUNYpwCQhwdwkM8PQ2CggIdnMO8o0w1I3wD7d0N7X00jXyN1TSSS6xMjQ1sLAwtrQwMrUwM9BJTEYTyK2wMqiNAgAVxBwI; cna=rP51EjQsYn0CAdIMPIL27G+U; _tb_token_=R3pVE1thAaFLsgD98ZDG; consoleRecentVisit=market; aliyun_choice=CN; _ga=GA1.2.970531576.1508839600; _gid=GA1.2.1392541234.1508839600; isg=Apubrnl2Rs2CE7o5bafCFW2lKvmpe7kQMAY-II3Q0hrtbItOE0ESwTSucPuY",
# "origin":"https://msp.aliyun.com",
# "referer":"https://msp.aliyun.com/isvDoc.htm?spm=5176.100135.d130.1.QB4Ak9",
# "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
# "x-requested-with":"XMLHttpRequest"
# }

# payload={"action":"createInstance","url":"http://demourl.com","orderBizId":"12345","orderId":"123456789","skuId":"yuncode215700000","aliUid":"12345678901234","email":"12345@aliyun.com","mobile":"13988888889","expiredOn":"2017-10-24 00:00:00"}

# print type(payload)
# res = requests.post(uri,data=payload,headers=header)


# if res.status_code == 200 and res.text != "":
# 	data = json.loads(res.text)
# 	print data['errorMsg']
# ":path":"/HomeAjax/GenerateIsvUrl.json",
# ":scheme":"https",
# ":authority":"msp.aliyun.com",
# ":method":"POST",