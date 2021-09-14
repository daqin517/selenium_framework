"""
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
"""
import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from utils.log import logger
from utils.config import REPORT_PATH

class Email():
    def __init__(self, server, sender, password, reciver, title, massage=None, path=None):
        '''
        初始化Email

        :param server: smtp服务器
        :param sender:发件人
        :param password:发件人密码
        :param reciver:收件人，多个收件人用“;”分号隔开
        :param title:邮件标题
        :param massage:邮件正文
        :param path:附件路径，可传入list（多个附件）或str（单个附件）
        '''
        self.server = server
        self.sender = sender
        self.password = password
        self.reciver = reciver
        self.title = title
        self.massage = massage
        self.file = path

        self.msg = MIMEMultipart('related')  # 带附件的邮件正文实例

    def attach_file(self, att_file):
        '''将单个文件添加到附件中'''
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {0}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.reciver

        # 邮件正文
        if self.massage:
            self.msg.attach(MIMEText(self.massage))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.file:
            if isinstance(self.file, list):
                for f in self.file:
                    self.attach_file(f)
            elif isinstance(self.file, str):
                self.attach_file(self.file)

        # 连接服务器并发送邮件
        try:
            stmp = smtplib.SMTP(self.server,25)
            # print(type(stmp))
        except error as e:
            logger.exception('发送邮件失败，无法连接SMTP服务器：',e)
        else:
            try:
                # stmp.connect(self.server, 25)
                # print('2222222')
                stmp.login(self.sender, self.password)
                print('login sucessful!!!')
            except smtplib.SMTPAuthenticationError as e:
            # except Exception as e:
                logger.exception('用户名密码验证失败！',e)
                # print('异常为：',e)
            else:
                stmp.sendmail(self.sender, self.reciver, self.msg.as_string())
            finally:
                stmp.quit()
                logger.info('发送邮件{0}成功，收件人：{1}'.format(self.title,self.reciver))


if __name__ == '__main__':
    report = REPORT_PATH + r'\testreport.html'
    e = Email('smtp.qq.com', '921497786@qq.com', 'dkomoybhicppbbdd', '921497786@qq.com', 'Test_Mail',massage='test（this is a massage!）',path=report)
    print('11111111')
    e.send()
