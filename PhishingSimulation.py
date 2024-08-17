import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'enter the sender email'
sender_password = 'create an app password and update it here'  #app pass
subject = 'Urgent: Action Required'

# Recipient email addresses
recipients = ['recipient1@gmail.com', 'recipient2@example.com']


message = MIMEMultipart('alternative')
message['From'] = sender_email
message['To'] = ''  # Usually the 'To' field will be the sender or left blank
message['Subject'] = subject

# Email body
email_content = """
<html>
<body>
    <p>Dear User,</p>
    <p>We have detected unusual activity in your account. Please verify your account by clicking on the link below:</p>
    <p><a href="example_url_where_u_want_to_redirect_the_user">Verify Now</a></p>
    <p>Regards,<br>IT Support</p>
</body>
</html>
"""
message.attach(MIMEText(email_content, 'html'))

try:
    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Send the email with BCC
    server.sendmail(sender_email, recipients, message.as_string())
    server.quit()
    print("Email sent successfully")
except Exception as e:
    print(f"Failed to send email: {str(e)}")
