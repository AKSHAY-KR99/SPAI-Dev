import smtplib
from email.mime.text import MIMEText

# Define the sender and receiver email addresses
sender_email = "spai05138@gmail.com"
receiver_email = "arathiashokan59@gmail.com"

# Define the email subject and body
subject = "SPAI Membership"
body = ("Hai Arathi Ashok\n"
        "We are glad to inform you that you successfully registered in SPAI.\n\n"
        "Secretery of SPAI\n"
        "Prof. Anil Ramachandran\n"
        "Sd/-")

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
server.login(sender_email, "cbycsxyyvldqrsrg")

# Send the email
server.sendmail(sender_email, receiver_email, msg.as_string())

# Close the SMTP connection
server.quit()

print("Email sent successfully!")
