import HTMLTestRunner
import os
import smtplib
import time
import unittest
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = formataddr(["发件人", "fangming@propersoft.cn"])
    msg['To'] = formataddr(["收件人", 'fangming@propersoft.cn'])
    msg['Subject'] = Header("测试报告", 'utf-8')

    smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    smtp.login("fangming@propersoft.cn", "a5SXz8frHACGmXuz")
    smtp.sendmail("fangming@propersoft.cn", "fangming@propersoft.cn", msg.as_string())
    smtp.quit()


def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './bbs/report/html/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='环境：winddows 10 浏览器： chrome')
    discover = unittest.defaultTestLoader.discover('./bbs/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./bbs/report/html/')
    send_mail(file_path)

