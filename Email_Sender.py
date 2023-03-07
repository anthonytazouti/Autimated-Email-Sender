#This program is an automated email sender through Python, you can think of it as a deconstructed email UI. You are able,
# to see all the components of the email. You are also able to see the imports such as SSL and smtplib.


from email.message import EmailMessage
from password import passsword
import ssl
import smtplib

#this is where you enter in your email, ex. youremail@gmail.com
emailSender = ""
#here you have to import your password
emailPassword = passsword

emailReceiver = "" #ex. yourfriendsemail@gmail.com

subject = "Anthony Tazouti Python Email Sender"
body = """
Hi, this is an email that is sent from a Python program!
"""

em = EmailMessage()
em ['From'] = emailSender
em ['To'] = emailReceiver
em ['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

#make sure you import your SMTP password
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailReceiver)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())
