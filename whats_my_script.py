#!/bin/python

from bs4 import BeautifulSoup as bs4
import requests
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

get_request = requests.get("http://www.ipvoid.com")
soup = bs4(get_request.content,'lxml')
ip = soup.find('input', {'name':''})['value']

# Turn on "Less Secure App for Google accounts. Refer - https://support.google.com/accounts/answer/6010255?hl=en"

fromaddr = "<YOUR GMAIL EMAIL ADDRESS>" 
toaddr = "<DESIRED EMAIL ADDRESS>"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Current IP is " + ip

server = smtplib.SMTP('smtp.gmail.com', 587) #change appropriate if using other than GMail
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, '<PASSWORD>')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
