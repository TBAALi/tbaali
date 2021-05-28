import datetime
import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务

mail_host="smtp.126.com"  #设置服务器
mail_user="jiaxx903@126.com"    #用户名
mail_pass="QHSEMNLGZMYVGABU"   #口令


sender = 'jiaxx903@126.com'
receivers = ['3107142922@qq.com']

a = 1
while a > 0:
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('Python 邮件发送测试—————— ' + str(a), 'plain', 'utf-8')
    message['From'] = Header(','.join(sender))   # 发送者
    message['To'] = Header(','.join(receivers))   # 接收者

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        a = a + 1
        print("邮件发送成功")

    except  Exception as e:
        print("Error: 无法发送邮件")
        print(str(e))

    #time.sleep(20)
    #a = 2
    print("Hello, World!")
    #while a > 0 :
        #now = datetime.date.today()
        #print(now)
        #a *= a
        #print(a)