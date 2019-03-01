# coding:utf-8

import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HuShi.Common.MailInfo import MailInfo
from HuShi.Common.GetLatestReport import GetLatestReport
import HuShi.Config.MailConfig


class SendMail:

    def __init__(self):
        self.file_new = GetLatestReport().getLatestPath()
        self.msg_from = HuShi.Config.MailConfig.msg_from
        self.passwd = HuShi.Config.MailConfig.passwd
        self.msg_to = HuShi.Config.MailConfig.msg_to

    def send(self,count,testTime):

        file_name = os.path.split(self.file_new)[1]
        content = MailInfo().getInfo(count,testTime)
        msg = MIMEMultipart("related")
        msgtext = MIMEText(content, _subtype="html", _charset="utf-8")  # 正文

        msg.attach(msgtext)
        # 添加附件
        att = MIMEText(open(self.file_new,"rb").read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = ('attachment; filename="{}"'.format(file_name))
        msg.attach(att)

        msg['Subject'] = "接口自动化测试报告"  # 主题
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to

        try:
            # 邮件服务器及端口号
            s = smtplib.SMTP_SSL(HuShi.Config.MailConfig.address,HuShi.Config.MailConfig.port)
            s.login(self.msg_from, self.passwd)
            s.sendmail(self.msg_from, self.msg_to, msg.as_string())

            print("邮件发送成功")
        except s.SMTPException as e:
            print("邮件发送失败")
        finally:
            s.quit()

if __name__ == "__main__":
    Send_Mail().Send(5)