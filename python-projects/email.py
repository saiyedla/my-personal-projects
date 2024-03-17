import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

logging.basicConfig(level=logging.DEBUG)

sender_email = "ysaireddi@gmail.com"
receiver_email = "contactkiran06@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."
attachment_path = r" Enter path here including file with externsion"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
attachment = open(attachment_path, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
message.attach(p)

smtp_server = "smtp.gmail.com"
smtp_port = 587  

password = "enter app password here"

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)  
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
except Exception as e:
    print("An error occurred:", e)
