import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
port = 25
msg = MIMEMultipart()
contxt = ssl.create_default_context()

smtp_server = "smtp.gmail.com"
sender_email = "tyrionwilldieins08@gmail.com"
password = 'gameofthrones'
receiver_email= ["kushgpt99@gmail.com"]

msg['from'] = sender_email
msg['subject'] = "Submission for Subtitles Selection."
bodytext = "Valar Morghulis\n"
msg.attach(MIMEText(bodytext, 'plain'))

for emailadd in receiver_email:
    print("connecting...")
    s = smtplib.SMTP(smtp_server, port)
    print("connected")
    s.starttls()
    print("logging in...")
    s.login(sender_email, password)
    print("logged in")
    print("sending mail to: ...\t"+emailadd, end="")
    msg['to'] = emailadd
    s.sendmail(sender_email, emailadd, msg.as_string())
    print("\tmail sent")
    s.quit()
