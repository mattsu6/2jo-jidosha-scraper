import smtplib
from email.mime.text import MIMEText
from config import Config

def send_mail(text, address):
  config = Config()
  msg = MIMEText(text)
  msg['Subject'] = '[予約監視] 通知'
  msg['From'] = config.mailer_name
  msg['To'] = address
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(config.mailer_name, config.mailer_pass)
  server.mail(config.mailer_name)
  server.rcpt(msg['To'])
  server.data(msg.as_string())
  server.quit()