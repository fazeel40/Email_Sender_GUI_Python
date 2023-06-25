import os
import smtplib
from email.message import EmailMessage
import ssl

emailsender = "fasghar40@gmail.com"
emailreceiver = "nouman02022@gmail.com" 
password = "wyqkrhafuaabdvub"
subject = "Spam Learning"
body = input("Enter your email: ")

em = EmailMessage()
em = emailsender
em = emailreceiver
em = subject

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465 ,context=context) as smtp:
    smtp.login(emailsender,password)
    smtp.sendmail(emailsender,emailreceiver,body)
    print("Email Sent!")