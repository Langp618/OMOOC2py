# coding-utf8-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import socket

class UdpServer(object):
	def tcpserver(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind(('', 9527))

		while True:
			recvData, (remoteHost, remotePort) = sock.recvfrom(1024)
			print("[%s:%s] connect: " % (remoteHost, remotePort))
	
			sendDataLen = sock.sendto("This is send data from server", (remoteHost, remotePort))
			print "recvData: ", recvData
			print "sendDataLen: ", sendDataLen
		sock.close()

if __name__ == "__main__":
	udpServer = UdpServer()
	udpServer.tcpserver()
		
