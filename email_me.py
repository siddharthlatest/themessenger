#! /usr/bin/env python

import httplib2
import getpass
import smtplib


from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run
from email.mime.text import MIMEText

def email(toaddrs, subject, body):
   fromaddress = 'getthemessenger@gmail.com'

   msg = MIMEText(body)
   msg['Subject'] = subject
   msg['From'] = fromaddress
   msg['To'] = toaddrs

   username = 'getthemessenger'
   password = 'chrissidd'
   server = smtplib.SMTP('smtp.gmail.com:587')

   server.starttls()
   server.login(username, password)
   server.sendmail(fromaddress, toaddrs, msg.as_string())
   server.quit()

if __name__ == '__main__':

   toaddrs = 'themessenger@mailinator.com'
   body = 'sample message\n'
   subject = "hello"
   email(toaddrs, subject, body)

