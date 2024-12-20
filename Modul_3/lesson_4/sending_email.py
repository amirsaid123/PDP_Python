import smtplib, ssl
import threading
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email):
    sender_email = "saidalosamigjonov071@gmail.com"
    password = "arrftauuaetbsuph"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    with open("D:\PDP Python\Modul_3\lesson_3\message.html") as f:
        html = f.read()

    part2 = MIMEText(html, "html")

    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    print(f"Email sent! {receiver_email}")


emails = ["amirsaidsamigjonov@gmail.com"]
start = time.time()
threads = []
for email in emails:
    t = threading.Thread(target=send_email, args=(email,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

    
print(time.time() - start)