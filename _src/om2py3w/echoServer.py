# coding=utf-8
# OMOOC_3
# version 1.1
# ubuntu/lang

import socket
import sys
import os
import diary

#define keyword as CMD
KEYWORDS = ['a', 'l', 'e', 'i']
'''
	Below CMD from client/ and response
	a = show history info and sent back to client;
	l = show newest info sent back to clinet;
	i = show new input input and record to dairy.log
	e = empty the log file
'''

#Based on Client command input process response
def response(keyword):
	if keyword.lowcase = 'a':
		dairy.showHistory()
		return 
	elif keyword.lowcase = 'l':
		dairy.showLine()
	elif keyword.lowcase = 'i':
		dairy.inputDiary()
	elif keyword.lowcase == 'e':
		emptyDiary()
	else: 
		return CMDerror


def main():
	
	#initial the daily.txt
	# if not exit daily.txt, built
	dairy.initDiary()
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
			data = "Error" + "无效命令，请输入正确指令：\n", + KEYWORDS
			sent = sendto(data, address)

		else:
			response(data)
			sent = sock.sendto(data, address)
			print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
