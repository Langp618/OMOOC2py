# coding=utf-8

import os

def append_text(text):
	f = open('dialy.txt','a+')
	f.write(text + '\n')
	f.close()

def get_text():
	if not os.path.exists('dialy.txt'):
		append_text('')
	else:
		f = open('dialy.txt')
		text = f.read()
		f.close()
		return text

if __name__ == '__main__':
	while True:
		text_input = raw_input('What do you want to write:\n>')
		if text_input.lower() in ['quit','q','exit']: break
		append_text(text_input)
		print "You diary:\n", get_text()
