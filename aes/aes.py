# #coding: utf8  
# import sys  
# from Crypto.Cipher import AES  
# from binascii import b2a_hex, a2b_hex  
import json

# class prpcrypt():  
# 	def __init__(self, key):  
# 		self.key = key  
# 		self.mode = AES.MODE_CBC  

# 	#加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数  
# 	def encrypt(self, text):  
# 		cryptor = AES.new(self.key, self.mode, self.key)  
# 		text = text.encode("utf-8")  
# 		#这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用  
# 		length = 16  
# 		count = len(text)  
# 		add = length - (count % length)  
# 		text = text + (b'\0' * add)  
# 		self.ciphertext = cryptor.encrypt(text)  
# 		#因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题  
# 		#所以这里统一把加密后的字符串转化为16进制字符串  
# 		return b2a_hex(self.ciphertext).decode("ASCII")  

# 	#解密后，去掉补足的空格用strip() 去掉  
# 	def decrypt(self, text):  
# 		cryptor = AES.new(self.key, self.mode, self.key)  
# 		plain_text = cryptor.decrypt(a2b_hex(text))  
# 		return plain_text.rstrip(b'\0').decode("utf-8")  

# if __name__ == '__main__':  
# 	pc = prpcrypt('keyskeyskeyskeys')      #初始化密钥  
# 	e = pc.encrypt("my book is free")  
# 	d = pc.decrypt(e)                       
# 	print (e, d)  
# 	e = pc.encrypt("我是一个粉刷匠1231繁體testひらがな")  
# 	d = pc.decrypt(e)                    
# 	print (e, d)   
{
	"device_id":"",
	"open_id":"oHcCdwvXP1zSMl_9QgchskQMNTf8",
	"union_id":"",
	"app_user_id":"",
	"deal_user_id":"bfe9ab0c-3bc8-49d2-8766-e23f68c14e52",
	"action":"",
	"description":"",
	"content":"",
	"client_info":"",
	"client_ip":"",
	"user_name":"zhuzhu",
	"user_title":"",
	"user_email":"",
	"user_phone":"",
	"user_company":"",
	"user_exts":""
}

{"device_id":"",
"open_id":"",
"union_id":"",
"app_user_id":"",
"deal_user_id":"bfe9ab0c-3bc8-49d2-8766-e23f68c14e52",
"name":"zhuzhu",
"title":"zhuzhu1",
"email":"",
"phone":"15210865171",
"company":"",
# "exts":"{"a":"b","c":"c"}",
"timestamp":"1548247342",
"sign":""}


# print(str(json.dumps({"a":"b","c":"c"})))

# import json
json={"device_id":"",
"open_id":"",
"union_id":"",
"app_user_id":"",
"deal_user_id":"bfe9ab0c-3bc8-49d2-8766-e23f68c14e52",
"name":"zhuzhu",
"title":"zhuzhu1",
"email":"",
"phone":"15210865171",
"company":"",
"exts":"{'a':'b','c':'c'}"
}

a = sorted(json.keys())
d = ""
for i in a:
	if json["%s"%i]=="":
		continue
	else:
		d += json["%s"%i]+":"
print(d)

# bfe9ab0c-3bc8-49d2-8766-e23f68c14e52:{"a":"b","c":"c"}:zhuzhu:15210865171:zhuzhu1:1548248089:abd27528-84c9-4bb4-80a3-4900b30d30f5

