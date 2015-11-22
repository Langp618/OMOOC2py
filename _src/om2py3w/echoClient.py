# coding=utf-8
# OMOOC2
# Version 1.1

import socket
import sys

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
data  = 'Hello, I am Client, Request~'

try:
	#send data
	print >> sys.stderr, 'Test server connection: "%s"' % data
	sent = sock.sendto(data, server_address)

	#Receive response
	print >>sys.stderr, 'Waiting to receive'
	data, server = sock.recvfrom(4096)
	print >>sys.stderr, 'received "%s" from Server' % data
	
	if 'Begin' in data:
		print >> sys.stderr, 'Good connection! Begin CMD:'
		if 'Error' not in data[0]:
			data = raw_input(">>")
			sent = sock.sendto(message, server_address)
		else:
			print "Error: ", data

finally:
	print >>sys.stderr, 'Closing socket'
	sock.close()
