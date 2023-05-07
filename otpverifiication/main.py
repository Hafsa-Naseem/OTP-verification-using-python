import random
import smtplib
from email.mime.text import MIMEText

def generate_otp():
 otp = random.randint(100000, 999999)
 return str(otp)

smtp_server = 'smtp.protonmail.com'
smtp_port = 465

ob = smtplib.SMTP_SSL(smtp_server, smtp_port)
ob.ehlo()
sender_password=input("Enter your password: ")
ob.login("otpverification11@proton.me",sender_password)

message = MIMEText("This is the OTP: " + generate_otp())
message['Subject'] = 'OTP'
message['From'] = 'otpverification11@proton.me'
message['To'] = input("Enter your email: ")

ob.sendmail(message['From'], message['To'], message.as_string())
ob.quit()
verify_otp = input("Enter the OTP to verify it: ")
if verify_otp == generate_otp():
 print("Correct OTP.")
else:
 print("Incorrect OTP. Please try again.")