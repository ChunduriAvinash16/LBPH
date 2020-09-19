import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as  pd
import os
def mail(filename1):
    from1 = "avinash200016@gmail.com"
    to = "chunduriavinash16@gmail.com"
    # instance of MIMEMultipart
    #df=pd.read_csv(filename1)
    #df.to_csv(filename1)
    data = MIMEMultipart()
# storing the senders email address
    data['From'] = from1
# storing the receivers email address
    data['To'] = to
# storing the subject
    data['Subject'] = "Subject of the Mail"
# string to store the body of the mail
    body = "Body-of-the-mail"
# attach the body with the msg instance
    data.attach(MIMEText(body, 'plain'))
# open the file to be sent
    filename = filename1
    attachment = open(filename1, "rb")
    #fileName = "Attendance"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    #attendance.to_csv(fileName, index=False)
# instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form
    p.set_payload((attachment).read())
# encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# attach the instance 'p' to instance 'msg'
    data.attach(p)
# creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
    s.starttls()
# Authentication
    s.login(from1, "9490484510")
# Converts the Multipart msg into a string
    text = data.as_string()
# sending the mail
    s.sendmail(from1, to, text)
    print("sucess")
# terminating the session
    s.quit()
