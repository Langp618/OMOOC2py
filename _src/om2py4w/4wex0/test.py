# coding: utf-8
from bottle import *

@route('/')
def index():
	return template('hallo.tpl'
		, title = 'LangDiary', hallo='你好吗？'
		)
debug(True)
run(host='127.0.0.1', port=8080, reloader=True)
