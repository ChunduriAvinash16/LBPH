import smtplib
import smtplib

gmail_user = 'avinash200016@gmail.com'
gmail_password = '9490484510'
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,"chunduriavinash16@gmail.com",'good morning')
except Exception as e:
    print('Something went wrong...')