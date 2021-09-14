import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from utils.config import CONFIG_FILE

mail_host = 'smtp.qq.com'
mail_port = 25
mail_user = '921497786@qq.com'
mail_code = 'wmqwzxpxwaigbfif'

sender = '921497786@qq.com'
receiver = ['zhouhe@chinatelecom.cn','yanqb@chinatelecom.cn','laohuatai@casachina.com.cn']

massage = MIMEMultipart()
massage = MIMEText('表锅们，\n\t周五不饮酒，青春喂了狗！wait for your chuiji!!!\n\nYour little cousin', 'plain', 'utf-8')  #邮件主体
# massage['From'] = Header('14级队长', 'utf-8')  #发件人别名
massage['From'] = sender
# massage['To'] = Header('13级小垃圾', 'utf-8')  #收件人别名
receiver = ';'.join(receiver)
print(receiver)
massage['To'] = receiver
subject = '出黎憋憋距'   #邮件主题 title
massage['Subject'] = Header(subject, 'utf-8')
# print(massage)
att = MIMEText(open(CONFIG_FILE,'rb').read(),'plain','utf-8')
att["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att["Content-Disposition"] = 'attachment; filename="test.txt"'
# massage.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.connect(mail_host, port=mail_port)
    smtp.login(mail_user, mail_code)
    smtp.sendmail(sender, receiver, massage.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送失败！！！')
    print('异常为：', e)
