from email.mime.text import MIMEText
from datetime import date
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "olivier.koch@gmail.com"
SMTP_PASSWORD = "NdrPrssr!1"

EMAIL_TO = ["olivier@olivierkoch.org"]
EMAIL_FROM = "email@gmail.com"
EMAIL_SUBJECT = "Demo Email : "

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "
EMAIL_BODY = "hey there"


def send_email(sender, receiver, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(receiver)
    msg['From'] = sender
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.ehlo()
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send_email(EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_BODY)
