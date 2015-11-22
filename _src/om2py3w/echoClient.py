# coding=utf-8
# OMOOC2
# Version 1.1

import socket
import sys

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message  = 'Hello, I am Client, Request~'

try:
	#send data
	print >> sys.stderr, 'sending "%s"' % message
	sent = sock.sendto(message, server_address)

	#Receive response
	print >>sys.stderr, 'Waiting to receive'
	data, server = sock.recvfrom(4096)
	print >>sys.stderr, 'received "%s" from Server' % data

	print >> sys.stderr, 'Good connection! Begin CMD:'

	message = raw_input(">>")
	sent = sock.sendto(message, server_address)

finally:
	print >>sys.stderr, 'Closing socket'
	sock.close()
