# coding=utf-8
# OMOOC_3
# version 1.0
#ubuntu/lang

import socket
import sys
import dialy

#define keyword as CMD
KEYWORDS = ['h/H', 's/S', 'n/N']
'''
	Below CMD from client/ and response
	h/H = show history info and sent back to client;
	s/S = show newest info sent back to clinet;
	n/N = show new input input and record to daily.txt
'''

#Based on Client command input process response
def response(keyword):
	if keyword.lowcase = 'h':
		daily.showHistory()
	elif keyword.lowcase = 's':
		daily.showNewest()
	elif keyword.lowcase = 'N':
		daily.recordNew()
	else: 
		print "无效命令，请输入正确指令：\n", KEYWORDS


def main():
	
	#initial the daily.txt
	# if not exit daily.txt, built
	daily.init()
	print "Config done!, Open Clinet, enter you command...."
	pirnt "..."
	print ''

	#create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	#Bind the socket to the port
	server_address = ('localhost', 10000)
	print >> sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	while True:
		print >>sys.stderr, '\nwaiting to receive message'
		data, address = sock.recvfrom(4960)

		print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
		print >>sys.stderr, data

		if data not in KEYWORDS:
			print "Error input"
			print >>sys.stderr, "Please enter command first: \n%s", KEYWORDS

		else:
			response(data)
			sent = sock.sendto(data, address)
			print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
