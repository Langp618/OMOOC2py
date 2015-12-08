# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: Lang
# email: penglbst@outlook.com

'''
Passistant Wechat Application
Personal tools
Web access: http://passistant.sinaapp.com/
Wechat platform: Passistant
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bottle import Bottle, request, route, run,template
import sae
import sae.kvdb #database
import time
#from time import localtime, strftime
import hashlib
import xml.etree.ElementTree as ET

app = Bottle()
kv = sae.kvdb.Client()

@app.route('/wechat')
def check_signature():
	'''
	wechat access verification
	'''
	token = "passistant" #wechat token
	signature = request.GET.get('signature',None)
	timestamp = request.GET.get('timestamp',None)
	nonce = request.GET.get('nonce',None)
	echostr = request.GET.get('echostr',None)
	L = [token,timestamp,nonce] #those three paramater to 
	L.sort()
	s=L[0]+L[1]+L[2]
	#tmpstr = "%s%s%s" % tuple(L) #same function
	if hashlib.sha1(s).hexdigest() == signature:
		return echostr
	else:
		return None

def parse_xml_msg():
	"""
	code for spliter wechat server post XML data
	"""
	recv_xml = request.body.read() #bottle
	root = ET.fromstring(recv_xml) #Element-tree
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg

## Below is function code
''' data sturcture
{'keyword':keyword,'username':username,'password':password}
'''

# wechat input 'l', then out all keyword/username list
# in below define: countkey = "key@" + str(count)

#read out all in wechat, web no read out feature
def read_all():
	temp = [i[1] for i in list(kv.get_by_prefix("key@"))]
	#temp is list of input line [{'key': 'keyword'...}, ... ]
	# list of dict out is key of dict
	#kv.get_by_prefix is yeild: (key, value)的tuple, i[1] = value
	#temp2 = sorted(temp1, key = lambda x:x['time'])
	temp2 = []
	for i in range(len(temp)):	
		key_user =str(i) +'. ' + temp[i]['keyword'] + ':' + temp[i]['username'] 
		i += 1
		temp2.apend(key_suer)
	#log = [temp2[i]['diary'] for i in range(len(temp2))]
	return temp2 

# based on keyword to read out the password
def read_keyword(keyword):
	temp = [i[1] for i in list(kv.get_by_prefix("key@")) if keyword in i[1]['keyword']]
	#keys is passowrd
	keys = [temp[i]['password'] for i in range(len(temp2))]
	return "\n".join(keys)

'''
def write_diary_wechat(raw_diary):
	#raw_diary = raw_diary.replace(" ","") #delete all whitespace
	withtag_diary = raw_diary.split('#') #split diary and tags by #
	newdiary = withtag_diary[0]
	if len(withtag_diary) == 1:
		tags = ["Wechat"]
	else:
		tags = withtag_diary[1:]
		tags.append("Wechat")
	
	count = len(read_diary_all()[0])
	countkey = "key@" + str(count) # key must be str()
	edit_time = strftime("%Y %b %d %H:%M", localtime())
	diary = {'time':edit_time,'diary':newdiary,'tags':tags}
	kv.set(countkey,diary)
'''

#write data to kvdb
# count is order 
def write_diary_web(keyword,username,password,count):
	countkey = "key@" + str(count)
	#edit_time = strftime("%Y %b %d %H:%M", localtime())
	# line 
	line = {'keyword':keyword,'username':username,'password':password}
	#line = {'order': count,'keyword':keyword,'username':username,'password':password}
	kv.set(countkey,line)

@app.route('/')
def start():
#	list_key_user = read_all()
#	return template("passistanSAE", diarylog=list_key_user )
	return template("passistantSAE")

@app.route('/', method='POST')
def input_new():

	keyword = request.forms.get('keyword')
	username = request.forms.get('username')
	password = request.forms.get('password')
	write_diary_web(keyword, username, passwod)
	return template("passistanSAE")

'''
#delete function developing
@app.route('/', method='DELETE')
def delete():
	temp = kv.getkeys_by_prefix("key@")
	for i in temp:
		kv.delete(i)
'''

##wechat
@app.route('/wechat', method = 'POST')
def response_wechat():
	'''
	response in wechat platform
	'''
	msg = parse_xml_msg()

	response_msg = '''
	<xml>
	<ToUserName><![CDATA[%s]]></ToUserName>
	<FromUserName><![CDATA[%s]]></FromUserName>
	<CreateTime>%s</CreateTime>
	<MsgType><![CDATA[text]]></MsgType>
	<Content><![CDATA[%s]]></Content>
	</xml>
	'''
	HELP = '''
	输入命令提示:
	- p = 进入关键字,帐号,密码输入界面,请点击开始
	- l = 列出所以的保存的用户名
		+ 然后输入数字会现实相应的用户名和密码
	- 关键字 = 根据关键子找出对于的帐号和密码
		+ 如: 淘宝: 13456@789.com --> mima987654321
	- h = help~
	'''

	if msg['MsgType'] == 'event':
		if msg['Event'] == 'subscribe':
			echo_str = HELP
			echo_msg = response_msg % (
				msg['FromUserName'],msg['ToUserName'],str(int(time.time())),echo_str)
			return echo_msg
	elif msg['MsgType'] == 'text':
		pass


	if msg['Content'].startswith('p'):
		pwdinput = msg['Content'][2:]
		write_diary_wechat(pwdInput)
		#count = len(read_diary_all()[0])
		echo_str = u"点击网页,按提示开始输入"
	elif msg['Content'] == 'l':
		echo_str = read_all()
	elif msg['Content'].replace(" ","").startswith('see#'):
		tags = msg['Content'].replace(" ","")[4:]
		tags = tags if tags else "Wechat"
		echo_str = read_diary_tags(tags)
	else:
		echo_str = HELP
		
	echo_msg = response_msg % (
		msg['FromUserName'],msg['ToUserName'],str(int(time.time())),echo_str)
	
	return echo_msg


application = sae.create_wsgi_app(app)
