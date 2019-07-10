# encoding:utf-8
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# b= [('mytext', u'1'), ('mypassword', u'2')]

# di={}
# for i in b:
# 	print i
# 	print type(i)
# 	di[str(i[0])]=str(i[1])
# print di.keys()

