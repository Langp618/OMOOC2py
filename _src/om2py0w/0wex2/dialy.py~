# coding=utf-8
# 0wd4 - 2015/11/15
# python2.7

import sys
import time

def main():
	#template:
	template = \
	'''
	##{modify_time}
	{content}
	'''

	modify_time = time.strftime("%b/%d/%Y %H:%M:%S")
	content = sys.argv[1:]
	##content += '\n'
	## below code use a template
	to_write = template.format(modify_time=modify_time, content=content)


	file = open('diary.txt', 'a+')## a+

	file.write(to_write)
	
	file.seek(0,0)
	print(file.read())

	file.close()

if __name__ == "__main__":
	main()
