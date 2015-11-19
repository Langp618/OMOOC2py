import socket
import sys

#create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message  = 'This is the message. It will be repeated.'

try:
	#send data
	print >> sys.stderr, 'sending "%s"' % message
	sent = sock.sendto(message, server_address)

	#Receive response
	print >>sys.stderr, 'Waiting to receive'
	data, server = sock.recvfrom(4096)
	print >>sys.stderr, 'received "%s"' % data

finally:
	print >>sys.stderr, 'Closing socket'
	sock.close()
