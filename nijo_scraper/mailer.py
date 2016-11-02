import smtplib
from email.mime.text import MIMEText

def send_mail(text, address):
  msg = MIMEText(text)

  msg['Subject'] = '[予約監視] 通知'
  msg['From'] = 'nijo@py.com'
  msg['To'] = address
  server = smtplib.SMTP('localhost')
  server.sendmail(msg['From'], msg['To'], msg.as_string())
  server.close()