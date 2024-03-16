import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
logging.basicConfig(level=logging.DEBUG)

# Email configuration
sender_email = "ysaireddi@gmail.com"
receiver_email = "contactkiran06@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create a MIMEText object for the email body
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# SMTP server configuration (for Gmail, replace with your SMTP server details)
smtp_server = "smtp.gmail.com"
smtp_port = 587  # TLS port

password = "rgrj ghbu pfhf ffse"

# Start a secure SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Start TLS encryption
    server.starttls()
    
    # Login to the SMTP server
    server.login(sender_email, password)  # Replace "your_password" with your email password
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")


