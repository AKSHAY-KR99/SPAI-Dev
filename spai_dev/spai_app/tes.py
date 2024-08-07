import smtplib
from email.mime.text import MIMEText

# Define the sender and receiver email addresses
sender_email = "akshayakr4@gmail.com"
receiver_email = "akshaydaskp121@gmail.com"

# Define the email subject and body
subject = "Cyber cell India Ltd"
body = ("Hi Akshay Das, "
        "You are under cyber cell surveillance. your phone activated illegal VPN several times for viewing porn web "
        "site. so you are under surveillance, please be vulnerable."
        "from department of Cyber Cell"
        "India")

# Create a text message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

# Define the SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create an SMTP connection
server = smtplib.SMTP(smtp_server, smtp_port)

# Start TLS encryption
server.starttls()

# Login to the SMTP server
server.login(sender_email, "fggartibcnylqtga")

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the SMTP connection
server.quit()

print("Email sent successfully!")
