from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
msg = MIMEMultipart()


msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
with open('C:/Users/cbf/Desktop/new_emotion.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'zzz623776013@outlook.com'
password = 'zcx123456'
to_addr = '623776013@qq.com'
to_addr2 = '459327959@qq.com'
smtp_server = 'smtp-mail.outlook.com'

import smtplib
server = smtplib.SMTP(smtp_server,587)

server.starttls()

msg['From'] = _format_addr('CBF<%s>' % from_addr)
msg['To'] = _format_addr('niubi<%s>' % to_addr)
msg['Subject'] = Header('こばんは','utf-8').encode()


server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
