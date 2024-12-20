import smtplib, ssl

port = 465
sender_email = "saidalosamigjonov071@gmail.com"
password = "arrftauuaetbsuph"
receiver_email = "supersuper.azizbek7@gmail.com"


context = ssl.create_default_context()
message = """
What`s up my nigga?
How are you doing dawg?
Is everything all right?
It is me Amirsaid from Thug Life.
"""
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email , receiver_email , message)
