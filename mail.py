import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
class mail():
    def __init__(self,user,password,to1,subject,text):
        self.user=user
        self.password=password
        self.text=text
        self.message_body = MIMEText(self.text, "plain")
        self.to1=to1
        self.subject=subject
        self.mail = smtplib.SMTP("smtp.gmail.com", 587)
        self.mail.ehlo()
        self.mail.starttls()
        self.message = MIMEMultipart()
    def send_mail(self):
        try:
            self.message["From"] = self.user
            self.message["To"] = self.to1
            self.message["Subject"] = self.subject
            self.message.attach(self.message_body)
            self.mail.login(self.user,self.password)
            self.mail.sendmail(self.message["From"], self.message["To"], self.message.as_string())
            self.mail.close()
        except:
            print("An error occured")
    def add_file(self,file,file_name):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename={}'.format(file_name))
        self.message.attach(part)
