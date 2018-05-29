#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
import smtplib,sys

mail_host = 'smtp.163.com'
mail_user = 'nicefeiniu@163.com'
mail_passwd = '53557873ly'

sender = 'nicefeiniu@163.com'
receivers = ['920036515@qq.com', '281188071@qq.com']

def send_mails():
    content = "Hello, my frend, where are you from? I'm from Rusha"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['From'] = mail_user
    msg['To'] = ",".join(receivers)
    msg['Subject'] = '人生苦短，我用python！！！！'

    try:
        smtp_em = smtplib.SMTP(mail_host)
        smtp_em.login(mail_user, mail_passwd)
        smtp_em.send_message(sender, receivers, str(msg))
        print('OK')
        smtp_em.quit()
    except smtplib.SMTPException as err:
        print(err)

if __name__ == '__main__':
    send_mails()