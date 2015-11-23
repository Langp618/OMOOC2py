# coding=utf-8
# OMOOC2
# Version 1.1

import socket
import sys

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
data  = ['Hello']

try:
	#send data
	print "Request server connection"
	sent = sock.sendto(data, server_address)

	#Receive response
	print >>sys.stderr, 'Waiting to receive'
	data, server = sock.recvfrom(4096)
	print >>sys.stderr, 'received "%s" from Server' % data
	
	if 'Begin' in data[0]:
		##Server change 'Hello' to 'begin'
		print >> sys.stderr, 'Good connection! Begin CMD:'
		if 'Error' not in data[1]: 
			##data[1] store CMD error flag
			data.append(raw_input("CMD: \n"))
			if 'i' in data[1]:
				## i means need typer to input at data[-1]
				data.append(raw_input("Enter what's you save here: "))
				sentInput = sock.sendto(data, server_address)
			else:
				sentCMD = sock.sendto(data, server_address)
		else:
			print "Error CMD: ", data

finally:
	print >>sys.stderr, 'Closing socket'
	sock.close()
