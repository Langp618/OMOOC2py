import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("baidu.com", 80))
print(s.getsockname()[0])
s.close()
