#-*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class SendMail:
    global send_user
    global email_host
    global password
    email_host = 'smtp.163.com'
    password = 'xie0716da'
    send_user="testcmallemail@163.com"
    def send_mail(self,user_list,sub,content):
        user = "xiehendga"+"<"+send_user+">"
        message=MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject']=sub
        message['From']=user
        message['To']=":".join(user_list)
        service=smtplib.SMTP()
        service.connect(email_host)
        service.login(send_user,password)
        service.sendmail(user,user_list,message.as_string())
        service.close()
    def send_main(self,pass_list,fail_list):
        passnum = int(len(pass_list))
        failnum = int(len(fail_list))
        countnum = passnum + failnum
        pass_result = "%.2f%%"%(passnum/countnum*100)
        fail_result = "%.2f%%"%(failnum/countnum*100)

        user_list = ['xiehengda@cydeng.com']
        sub = '接口自动化测试报告'
        content = "此次一共运行接口个数为%s个,通过个数为%s个,失败个数为%s个,通过率为%s,失败率为%s"%(countnum,passnum,failnum,pass_result,fail_result)
        self.send_mail(user_list, sub, content)

