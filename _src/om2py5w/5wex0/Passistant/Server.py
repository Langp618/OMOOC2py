# coding=utf-8
# Version 4.2
# base on bottle.py 

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import route, run, request, debug, template
from diary import showHistory, inputDiary
import os
import time
import sqlite3

#write diary to database
def write_db(post):
	conn = sqlite3.connect('webDiary.db')#open db connect
	cur = conn.cursor()
	cur.execute('INSERT INTO lan (time, content) VALUES  (?, ?);', (time.time(), unicode('post'))) 
	cur.close()
	conn.commit()
	con.close()

# read db
def get_db():
	conn = sqlite3.connect('webDiary.db')
	cur = conn.cursor()
	cur.execute('SELECT time,content FROM lan ORDER BY time DESC;')
	results = cur.fetchall() #返回剩余的行
	cur.close()
	conn.close()
	return results

##route
@route('/')
@route('/write')
def write():
	mydiary = get_db()
	return template('webdiary.tpl', item=mydiary)

@route('/write', method='POST')
def to_write():	
	newdiary = request.forms.get('txtadd')
	write_db(newdiary)
	mydiary = get_db()
	return template('webdiary.tpl', item=mydiary)

#client
@route('/read_raw')
def read_raw():
	content = ''
	conn = sqlite3.connect('webDiary.db')
	cur = conn.cursor()
	cur.execute('SELECT content FROM lang;')
	content = '\n'.join([row[0].encode('utf-8') for row in cur.fetchall()])
	cur.close()
	conn.close()
	return content


if __name__ == '__main__':
	debug(True)
	run(host='localhost', port=8080, reloader=True)
	
