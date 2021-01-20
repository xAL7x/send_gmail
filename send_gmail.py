import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os.path

email=input("enter the from email --> ")
password=input(str("enter the password -->"))
send_email=input("enter the send email --> ")
subject=input("enter the subject --> ")
msg=MIMEMultipart()
msg['From']=email
msg['To']=send_email
msg['Subject']=subject
print(" text(1) file(2)")
a=input('what do you want send ? \n')
if a=="1":
    message=input("enter the message : ")
    q=input("do you want add file? [y/n]\n")
    if q=="y" or q=="yes":
        msg.attach(MIMEText(message,'plain'))
        file=input("enter the file location \n")
        filename=os.path.basename(file)
        attachment=open(file,"rb")
        part=MIMEBase("application","octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition","attachment;filename=%s"%filename)
        msg.attach(part)
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("login is found")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
        server.quit()
    if q=="n" or q=="no":
        msg.attach(MIMEText(message,'plain'))
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        print("login is found")
        text=msg.as_string()
        server.sendmail(email,send_email,text)
if a=="2":
    file=input("enter the file location \n")
    filename=os.path.basename(file)
    attachment=open(file,"rb")
    part=MIMEBase("application","octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment;filename=%s"%filename)
    msg.attach(part)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    print("login is found")
    file=msg.as_string()
    server.sendmail(email,send_email,file)
    server.quit()
