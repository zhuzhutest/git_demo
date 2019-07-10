import smtplib  
import sys  
import email.mime.text  
# my test mail  
mail_username='XXXXXXX@XXXXXX.com'
mail_password='ABC123'
from_addr = mail_username  
to_addrs=('XXXXXXX@XXXXXX.com')
  
# HOST & PORT  
HOST = 'smtp.gmail.com'  
PORT = 25  
  
# Create SMTP Object  
smtp = smtplib.SMTP()  
print 'connecting ...'  
  
# show the debug log  
smtp.set_debuglevel(1)  
  
# connet  
try:  
    print smtp.connect(HOST,PORT)  
except:  
    print 'CONNECT ERROR ****'  
# gmail uses ssl  
smtp.starttls()  
# login with username & password  
try:  
    print 'loginning ...'  
    smtp.login('XXXXXXX@XXXXXX.com','XXXXXXX')
except:  
    print 'LOGIN ERROR ****'  
# fill content with MIMEText's object   
msg = email.mime.text.MIMEText('Hi ,I am leehark')  
msg['From'] = from_addr  
msg['To'] = ';'.join(to_addrs)  
msg['Subject']='hello , today is a special day'  
print msg.as_string()  
smtp.sendmail(from_addr,to_addrs,msg.as_string())  
smtp.quit()