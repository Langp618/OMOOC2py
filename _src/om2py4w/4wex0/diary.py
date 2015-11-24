# coding=utf-8

import os
import time
import sys

#from docopt import docopt

"""diary.py

Usage:
	diary.py [Options]
	diary.py (-h | --help)
	diary.py --version

Options:
	-a --history  shows all history record
	-l --line     shows newest line info
	-i --input    record new info input
	-e --empty    empty log file
"""

KEYWORDS = ['a','l','i','e']

#init dialy.log
def initDiary():

	TIME = time.strftime('%b %d %Y') 
	TITLE = 'This is diary log, built time：'
	if not os.path.exists('diary.log'):
		f = open('diary.log', 'a')
		# 'a', if files exit, read/
		# if not exist built new
		# only write, can't read
		f.write(TITLE + TIME)
		print "Built diary.log file, New~"
#	f = open('diary.log', 'a')
		f.write('\n#######\n')
		f.close()
	
	print "diary.log init successful.."	

def emptyDiary():
	f = open('diary.log', 'w+')
	# w+ clean previous files
	f.write('')
	f.close()
	
def showHistory():
	f = open('diary.log', 'r')
	## r begin of files, only read
	f.seek(0, 0)
	print f.read()
	f.close()

def showLine():
	print "This function in developing"

"""	f = open('diary.log', 'r')
	fLen = len(f.readlines())
	line = f.seek(fLen)   ??
	print line
	f.close()
"""

def inputDiary(data):
	# Adding the time info in previous data
	data = time.strftime('%b %d %Y') +': ' +data;

	# write to files
	f = open('diary.log', 'a+')
	# 'a+' = a + w, begin of end of file
	f.write(data + '\n--------\n')
	f.close()

'''
def get_text():
	if not os.path.exists('diary.txt'):
		append_text('')
	else:
		f = open('diary.txt')
		text = f.read()
		f.close()
		return text
'''


if __name__ == '__main__':
	initDiary()
	
	#arguments = docopt(__doc__, sys.argv[1:])
	arguments = sys.argv[1]

	if arguments == 'a':
		showHistory()
	elif arguments == 'l':
		showLine()
	elif arguments == 'i':
		data = raw_input(">> ")
		inputDiary(data)
	elif arguments == 'e':		
		emptyDiary()
	else:
		print "Error argument, make sure argv in ", KEYWORDS
