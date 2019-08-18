import urllib
import smtplib
response = urllib.urlopen("https://wordpress.com/start/ar/?ref=homepage")
data = response.read()
print data

sender = input("Enter your Email : ")
password = input("Enter the Password : ")
receiver = input("Enter your Receiver : ")
message = input("Enter your Message : ")
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender,password)
    server.sendmail( sender ,receiver,  message)
    server.quit()
    print ' sent Successfully'
except:
    print ' there is error '