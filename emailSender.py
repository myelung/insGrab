import smtplib
from email.mime.text import MIMEText
from email.header import Header

message = MIMEText('Hello Boy!')
message['From'] = Header('1244639510@qq.com')
message['To'] = Header('NIN')
message['Subject'] = Header('WHAT?')

mail = smtplib.SMTP()
mail.connect("smtp.qq.com")
mail.login("1244639510@qq.com", "bhkyyxzsezelheec")
mail.sendmail("1244639510@qq.com", ["myralon1997@163.com"], message.as_string())