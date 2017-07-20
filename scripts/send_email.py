import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from email.MIMEText import MIMEText

fromaddrs = 'helderjunior9@gmail.com'  
 
files = "C:\Users\helder.rodrigues\Dropbox\Cabrini\certificados"
emails = file("C:\Users\helder.rodrigues\Dropbox\Cabrini\email.txt")

# Credentials (if needed)  
username = 'helderjunior9'  
password = 'junior010295'  

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  

SUBJECT = "Workshop USP/IoT 2016: Desafios em Conectividade para IoT"
cf = file('C:\Users\helder.rodrigues\Dropbox\Cabrini\\content.txt')
content = cf.read()
cf.close()

body = MIMEText(content,'plain')

for x in range(1,36):
	emails.readline()

for cert in range(36,95):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = SUBJECT 
	msg['From'] = fromaddrs

	cert_local = files+ "\\" + str(cert)+".pdf"
	toaddrs = emails.readline().strip()

	print "email to send: " + toaddrs
	print "cert: " + cert_local
	msg['To'] = toaddrs
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(cert_local , "rb").read())
	Encoders.encode_base64(part)

	part.add_header('Content-Disposition', 'attachment; filename="certificado.pdf"')
	msg.attach(body)
	msg.attach(part)
	try:
		server.sendmail(fromaddrs, toaddrs, msg.as_string())
		print "Email sent"
	except Exception:
		print "ERROR WHILE SENDING EMAIL"
		pass
	print
	msg = None

server.quit()
