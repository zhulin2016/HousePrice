import subprocess
import os
import commands
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib



os.chdir('/home/ubuntu/workplace/linkhome')
subprocess.call(["scrapy","crawl","linkhome1"])
subprocess.call(["scrapy","crawl","linkhome2"])
date = commands.getoutput('date "+%Y_%m_%d %H:%M:%S"')
date += ".csv"
subprocess.call(["scrapy","crawl","linkhome3","-o",date,"-t","csv"])

msg = MIMEMultipart()
att1 = MIMEText(open(date,'rb').read(), 'base64', 'gb2312')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename=\''+date+'\''
msg.attach(att1)

sendToList = ['zhulinbjtu@163.com','1424380402@qq.com','54483460@qq.com','sunmall@yeah.net']
msg['to'] = ";".join(sendToList)
msg['from'] = 'Gorgeous<1424380402@qq.com>'
msg['subject'] = date
try:
	server = smtplib.SMTP()
	server.connect('smtp.qq.com')
	server.login('1424380402','ocydvzaggrijbadd')
	server.sendmail(msg['from'], sendToList, msg.as_string())   #if u use "msg['to']" here, u will send mail only to the first one.  And this is a bug of python's sending e-mail to many address. u must use "sendToList" here to achieve ur goal.
	server.quit()
	print 'send success'
except Exception, e:
	print str(e)

