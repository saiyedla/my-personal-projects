import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
logging.basicConfig(level=logging.DEBUG)

sender_email = "ysaireddi@gmail.com"
receiver_email = "contactkiran06@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

smtp_server = "smtp.gmail.com"
smtp_port = 587  

password = " "

# Start a secure SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:

    server.starttls()
    

    server.login(sender_email, password)  
    
  
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")


