# coding = utf-8
# OMOOC4W
# Use bottle as template
# version 4.0


from bottle import run, template, route, debug, request
from diary import inputDiary, showHistory

@route('/')
@route('/write')
def write():
	mdiary = showHistory()
	# write.tpl is template for this code
	return template('write.tpl', diary=mdiary)

@route('/write', method='POST')
def do_write():
	diary_log = request.forms.get('diary_log')
	inputDiary(diary_log) #read in
	mydiary = showHistory() # read out to shows
	return template('write.tpl', diary=mydiary)

@route('/readout')
def readout():
	f = open('diary.log')
	content = f.read()
	f.close()
	return content

if __name__ == '__main__':
	debug(True)
	run(host='localhost', port=8080, reloader=True)
