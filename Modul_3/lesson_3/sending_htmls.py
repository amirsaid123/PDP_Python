import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "saidalosamigjonov071@gmail.com"
receiver_email = "supersuper.azizbek7@gmail.com"
password = "arrftauuaetbsuph"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email



with open("message.html" ) as f:
    html = f.read()


part2 = MIMEText(html, "html")

message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )