import os
import shutil
import smtplib
from email.mime.text import MIMEText

# Rename multiple files in a directory
file_list = os.listdir('directory_path')
for filename in file_list:
if filename.endswith('.txt'):
new_filename = filename.replace('old_text', 'new_text')
os.rename(filename, new_filename)

# Send an automated email
sender_email = 'sender@example.com'
receiver_email = 'receiver@example.com'
message = MIMEText('This is the body of the email.')
message['Subject'] = 'Automated Email'
message['From'] = sender_email
message['To'] = receiver_email

with smtplib.SMTP('smtp.example.com', 587) as server:
server.login('username', 'password')
server.sendmail(sender_email, receiver_email, message.as_string())
