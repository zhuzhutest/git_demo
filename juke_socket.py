import socket
import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected!')

@sio.on('message')
def on_message(data):
    print('I received a message!')

@sio.on('my message')
def on_message(data):
    print('I received a custom message!')

@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')

sio.connect('wss://juke-test3-node1.kuick.cn:1316')
print('my sid is', sio.sid)
# 创建一个客户端的socket对象
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 设置服务端的ip地址
# host = "wss://juke-test3-node1.kuick.cn"
# # 设置端口
# port = 1316
# # 连接服务端
# client.connect((host, port))
#
# # while循环是为了保证能持续进行对话
# while True:
#     # client.send(sendmsg.encode("utf-8"))
#     msg = client.recv(1316)
#     # 接收服务端返回的数据，需要解码
#     print(msg.decode("utf-8"))
# # 关闭客户端
# client.close()