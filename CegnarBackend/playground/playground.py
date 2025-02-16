import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "test@cegnarblacksmithing.com"
receiver_email = "vid@pesko.com"

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = "Hi, www.realpython.com"

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP_SSL(
    host="h130.hitrost.net",
    port=465
)

s.login("test@cegnarblacksmithing.com", "Testpassword123")

s.sendmail("test@cegnarblacksmithing.com", ["vid@pesko.si"], message.as_string())
s.quit()
