# coding=utf-8
# 0wd4 - 2015/11/15
# python2.7

import sys

def main():
	content = sys.argv[1]
	content += '\n'

	file = open('diary.txt', 'a+')

	file.write(content)
	
	file.seek(0,0)
	print(file.read())

	file.close()

if __name__ == "__main__":
	main()
