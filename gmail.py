# Python code to illustrate Sending mail from 
# your Gmail account 
from os import name
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication




#The mail addresses and password
sender_address = 'jandginvestment@gmail.com'
# https://myaccount.google.com/u/1/security
sender_pass = 'vdkjdevbsgmoinpv'
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
with open('2addresses.csv','r') as file:
    addresses=csv.reader(file)
    for address in addresses:
        receiver_address = address[0]
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Seeking .NET/ Angular full stack consultant openings in Dubai/ Sharjah/ Ajman/Abhudhabi'   #The subject line
        #The body and the attachments for the mail
        # read mail content from a html file
        f = open("body1.html", 'r', encoding='utf-8').read()
        mail_content =str( f).replace('{{Name}}',receiver_address.split('@')[0].split('.')[0].capitalize())
        message.attach(MIMEText(mail_content, 'html'))
        filename = "jandg.docx"
        with open(filename,'rb') as attach:
            message.attach(MIMEApplication(attach.read(),name=filename))
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        print(address[0])
session.quit()
print('Mail Sent')

